from django.urls import path
from . import views

urlpatterns= [
    # path('', views.login, name= 'login'),
    path('register', views.register, name= 'register'),
    path('index', views.index, name= 'index'),
    path('add', views.add_food, name= 'add'),
    path('order/<str:item>', views.order, name= 'order'),
    path('checkout/<str:item>', views.checkout, name= 'checkout'),
    path('cart/<str:user>/<str:item>', views.cart, name= 'cart'),
    path('cart/<str:user>', views.view_cart, name= 'view_cart'),
    path('delete_item/<str:item>', views.delete_item, name= 'delete_item'),
    path('menu', views.menu, name= 'menu'),
    path('about', views.about, name= 'about'),
    path('contact', views.contact, name= 'contact'),
]