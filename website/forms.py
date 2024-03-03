from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Client, Order

#Регистрация
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email адрес'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Имя'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Фамилия'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Имя пользователя'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''


class AddClientForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Имя", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Фамилия", "class":"form-control"}), label="")
    email = forms.CharField(required=True, max_length=100, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Телефон", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Город", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Адрес", "class":"form-control"}), label="")

    class Meta:
        model = Client
        fields = '__all__'

class AddOrderForm(forms.ModelForm):
    product_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Товар", "class":"form-control"}), label="")
    color = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Цвет", "class":"form-control"}), label="")
    producer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Производитель", "class":"form-control"}), label="")
    price = forms.DecimalField(required=True, max_digits=10, decimal_places=2, widget=forms.widgets.TextInput(attrs={"placeholder":"Цена", "class":"form-control"}), label="")
    margin = forms.DecimalField(required=True, max_digits=10, decimal_places=2, widget=forms.widgets.TextInput(attrs={"placeholder":"Наценка", "class":"form-control"}), label="")
    client_name = forms.ModelChoiceField(queryset=Client.objects.all(), label="Имя клиента")
    
    class Meta:
        model = Order
        fields = '__all__'

class OrderedOrders(forms.Form):
    choices = [
        ["price", "Цена по возрастанию"],
        ["-price", "Цена по убыванию"],
        ["product_name", "По названию"],
    ]
    ordering = forms.ChoiceField(label="", choices=choices)   

class OrderedClients(forms.Form):
    choices = [
        ("first_name", "Имена по возрастанию"),
        ("-first_name", "Имена по убыванию"),
        ("created_at", "По дате по убыванию"),
        ("-created_at", "По дате по возрастанию"),
        ("city", "По городам по возрастанию"),
        ("-city", "По городам по убыванию"),  
    ]
    ordering = forms.ChoiceField(label="", choices=choices)   
