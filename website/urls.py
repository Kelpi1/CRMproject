from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60*15)(views.home), name='home'),
    # path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('client/<int:pk>', views.client_record, name='client'),
    path('delete_client/<int:pk>', views.delete_client, name='delete_client'),
    path('add_client/', views.add_client, name='add_client'),
    path('update_client/<int:pk>', views.update_client, name='update_client'),
    path('search_client/', views.search_client, name='search_client'),

    path('order_list/', views.order_list, name='order_list'),
    path('order/<int:pk>', views.order, name='order'),
    path('delete_order/<int:pk>', views.delete_order, name='delete_order'),
    path('add_order/', views.add_order, name='add_order'),
    path('update_order/<int:pk>', views.update_order, name='update_order'),
    path('search_order/', views.search_order, name='search_order'),

]