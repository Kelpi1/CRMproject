from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddClientForm, AddOrderForm, OrderedOrders, OrderedClients
from .models import Client, Order
from django.db.models import Q

def home(request):
    clients = Client.objects.all()
    orders = Order.objects.all()
    form = OrderedClients(request.GET)
    if request.user.is_authenticated:
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                clients = clients.order_by(form.cleaned_data["ordering"])
        context = {'clients':clients, 'form': OrderedClients(), 'orders':orders}
        return render(request, 'home.html', context)

    #Проверка авторизации
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Авторизация
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы авторизованы!")
            return redirect('home')
        else:
            messages.success(request, "Ошибка авторизации, попробуйте снова...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'clients':clients})

def logout_user(request):
    logout(request)
    messages.success(request, "Вы вышли из системы!")
    return redirect('home')
    
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Аутентификация и авторизация 
            username = form.cleaned_data['username']
            password = password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            #login(request, user)
            messages.success(request, "Вы успешно зарегистрированы!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})


def client_record(request, pk):
    try:
        if request.user.is_authenticated:
            client_record = Client.objects.get(id=pk)
            order = Order.objects.get(client_name_id=client_record.id)
            return render(request, 'client.html', {'client_record':client_record, 'order':order})
        else:
            messages.success(request, "Вы должны быть авторизованы для просмотра записей")
            return redirect('home')
    except Order.DoesNotExist:
            if request.user.is_authenticated:
                client_record = Client.objects.get(id=pk)
                return render(request, 'client.html', {'client_record':client_record})
            else:
                messages.success(request, "Вы должны быть авторизованы для просмотра записей")
                return redirect('home')
    except Order.MultipleObjectsReturned:
        if request.user.is_authenticated:
            client_record = Client.objects.get(id=pk)
            order = Order.objects.filter(client_name_id=client_record.id).order_by('id').first()
            return render(request, 'client.html', {'client_record':client_record, 'order':order})
        else:
            messages.success(request, "Вы должны быть авторизованы для просмотра записей")
            return redirect('home')


def delete_client(request, pk):
    if request.user.is_authenticated:
        delete_it = Client.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Запись удалена")
        return redirect('home')
    else:
        messages.success(request, "Для этого действия вы должны быть авторизованы...")
        return redirect('home')


def add_client(request):
    form = AddClientForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_client = form.save()
                messages.success(request, "Запись добавлена")
                return redirect('home')
        return render(request, 'add_client.html', {'form':form})
    else:
        messages.success(request, "Для этого действия вы должны быть авторизованы...")
        return redirect('home')


def update_client(request, pk):
    if request.user.is_authenticated:
        current_client = Client.objects.get(id=pk)
        form = AddClientForm(request.POST or None, instance=current_client)
        if form.is_valid():
            form.save()
            messages.success(request, "Запись обновлена!")
            return redirect('home')
        return render(request, 'update_client.html', {'form':form})
    else:
        messages.success(request, "Для этого действия вы должны быть авторизованы...")
        return redirect('home')


def search_client(request):
    if request.method == "POST":
        searched = request.POST['searched']
        clients = Client.objects.filter(Q(first_name__icontains=searched) |
        Q(last_name__icontains=searched) |
        Q(email__icontains=searched) |
        Q(city__icontains=searched) |
        Q(address__icontains=searched) | 
        Q(phone__icontains=searched) |
        Q(created_at__icontains=searched))
        return render(request, 'search_client.html', {'searched':searched, 'clients':clients})
    else:
        return render(request, 'search_client.html', {})


##########################
def order_list(request):
    orders = Order.objects.all()
    clients = Client.objects.all()
    form = OrderedOrders(request.GET)
    if request.user.is_authenticated:
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                orders = orders.order_by(form.cleaned_data["ordering"])
        context = {'orders':orders, 'form': OrderedOrders(), 'clients':clients,}
        return render(request, 'order_list.html', context)
    else:
        messages.success(request, "Для этого действия вы должны быть авторизованы...")
        return redirect('home')



def order(request, pk):
    if request.user.is_authenticated:
        order = Order.objects.get(id=pk)
        client = Client.objects.get(id=order.client_name_id)
        return render(request, 'order.html', {'order':order, 'client':client})
    else:
        messages.success(request, "Вы должны быть авторизованы для просмотра записей")
        return redirect('home') 


def delete_order(request, pk):
    if request.user.is_authenticated:
        delete_order = Order.objects.get(id=pk)
        delete_order.delete()
        messages.success(request, "Запись удалена")
        return redirect('order_list')
    else:
        messages.success(request, "Для этого действия вы должны быть авторизованы...")
        return redirect('home')


def add_order(request):
    form = AddOrderForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_order = form.save()
                messages.success(request, "Запись добавлена")
                return redirect('order_list')
        return render(request, 'add_order.html', {'form':form})
    else:
        messages.success(request, "Для этого действия вы должны быть авторизованы...")
        return redirect('home')


def update_order(request, pk):
    if request.user.is_authenticated:
        current_order = Order.objects.get(id=pk)
        form = AddOrderForm(request.POST or None, instance=current_order)
        if form.is_valid():
            form.save()
            messages.success(request, "Запись обновлена!")
            return redirect('order_list')
        return render(request, 'update_order.html', {'form':form})
    else:
        messages.success(request, "Для этого действия вы должны быть авторизованы...")
        return redirect('home')


def search_order(request):
    if request.method == "POST":
        searched = request.POST['searched']
        orders = Order.objects.filter(Q(product_name__icontains=searched) |
        Q(producer__icontains=searched) |
        Q(price__icontains=searched) |
        Q(margin__icontains=searched) | 
        Q(created_at__icontains=searched))


        return render(request, 'search_order.html', {'searched':searched, 'orders':orders})
    else:
        return render(request, 'search_order.html', {})
    

    