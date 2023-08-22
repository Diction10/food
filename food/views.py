from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, LoginForm, AddFoodForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import *
from django.contrib import messages
from datetime import date

# homepage
@login_required
def index(request):
    # display images from the db
    imgs = Food.objects.all()
    imgs = [imgs[i:i + 3] for i in range(0, len(imgs), 3)]


    return render (request, 'food/index.html', {'imgs': imgs})


# register function
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            # messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'food/register.html', {'form': form})


# add food item function
@login_required
def add_food(request):
    if request.method == 'POST':
        form = AddFoodForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
           
            return redirect('index')
    else:
        form = AddFoodForm()
    return render(request, 'food/add.html', {'form': form})


@login_required
def order(request, item):
    food_item = Food.objects.get(name=item)

    return render (request, 'food/order.html', {'food_item' : food_item})


@login_required
def checkout(request, item):
    detail = Food.objects.get(name=item)
    today = date.today()
   
    quantity = 1
    

    total = int(detail.price) * quantity


    return render (request, 'food/checkout.html', {
        'detail' : detail, 
        'total':total,
        'today': today
    })


@login_required
def cart(request, user, item):
    item = Food.objects.get(name=item)
    items = Cart.objects.filter(user = request.user)
        
    cart_item = Cart()

    quantity = request.POST['quantity']
    amount = item.price * int(quantity)

    cart_item = Cart.objects.create(quantity = quantity, amount = amount )
    cart_item.food_name.set([item.id])
    cart_item.user.set([request.user])

    cart_item.save()    

    return render (request, 'food/cart.html', {'items':items })



@login_required
def view_cart(request, user):
    items = Cart.objects.filter(user = request.user)
  
    return render (request, 'food/cart.html', {'items' : items})


@login_required
def delete_item(request, item):
    item = Cart.objects.get(id=item)

    # Delete the item
    item.delete()
    item.save()
    messages.success(request, f'Item deleted from cart successfully!!')
    return HttpResponseRedirect(reverse("index"))
    

@login_required
def menu(request):
    food_items = Food.objects.all()
    food_items = [food_items[i:i + 3] for i in range(0, len(food_items), 3)]

    return render(request, 'food/menu.html',{'food_items':food_items})

@login_required
def about(request):
    return HttpResponse('about')

@login_required
def contact(request):
   if request.method == 'POST':
     messages.success(request, f'Message sent successfully!!')
     return HttpResponseRedirect(reverse("index"))
   return render(request, 'food/contact.html')
   
    

    
