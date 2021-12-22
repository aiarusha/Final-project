from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from myApp.forms import UserRegisterForm


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'myApp/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'myApp/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def home(request):
    return render(request, 'myApp/home.html')


def men(request):
    return render(request, 'myApp/men.html')


def women(request):
    return render(request, 'myApp/women.html')


def aboutus(request):
    return render(request, 'myApp/aboutus.html')


def signUpPage(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            useremail = form.cleaned_data.get('email')
            userid = User.objects.filter(username=username).first().id
            customer = Customer.objects.create(name=username, email=useremail, user_id=userid)
            customer.save()
            messages.success(request, 'Account was created for ' + username)

        return redirect('login')

    context = {'form': form}
    return render(request, 'myApp/register.html', context)


def signInPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Username or password is incorrect!')

    return render(request, 'myApp/login.html')


def signOutPage(request):
    logout(request)
    return redirect('home')


def contact(request):
    return render(request, 'myApp/contact.html')


def skincare(request):
    return render(request, 'myApp/skincare.html')


def sales(request):
    return render(request, 'myApp/sales.html')


def new(request):
    return render(request, 'myApp/new.html')
