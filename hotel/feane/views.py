from django.shortcuts import render,redirect
from .models import Product,description
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.http import HttpResponse
import logging

# Create your views here.
def index(request):
    
    # d1=description()
    # d1.id=1
    # d1.mtitle="pizza"
    # d1.iimg="p2.png"
    # d1.price=4
    # d1.desc="a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients"


    # d2=description()
    # d2.id=2
    # d2.mtitle="Non pizza"
    # d2.iimg="p1.png"
    # d2.price=4
    # d2.desc="a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients"

    # d3=description()
    # d3.id=3
    # d3.mtitle="Chicken burger"
    # d3.iimg="f2.png"
    # d3.price=4
    # d3.desc="Juicy, big, loaded with toppings of my choice." "High quality beef medium to well with cheese and bacon on a multigrain bun." "A huge single or triple burger with"


    # d4=description()
    # d4.id=4
    # d4.mtitle="Mexicon burger"
    # d4.iimg="f2.png"
    # d4.price=4
    # d4.desc="Juicy, big, loaded with toppings of my choice.""High quality beef medium to well with cheese and bacon on a multigrain bun." "A huge single or triple burger with"


    # d5=description()
    # d5.id=5
    # d5.mtitle="frinch frys"
    # d5.iimg="f1.png"
    # d5.price=4
    # d5.desc="french fries, also called chips, finger chips, fries, or French pommes frites, side dish or snack made from deep-fried potatoes that have been cut into pices."


    # d6=description()
    # d6.id=6
    # d6.mtitle="pizza"
    # d6.iimg="pizza.jpg"
    # d6.price=4
    # d6.desc="french fries, also called chips, finger chips, fries, or French pommes frites, side dish or snack made from deep-fried potatoes that have been cut into pices."


    # dlists=[d1,d2,d3,d4,d5,d6]

    dlist=description.objects.all()
    plist=Product.objects.all()
    return render (request,"index.html",{'dlists':dlist,'plists':plist})


#cart views


@login_required(login_url="/users/login")
def cart_add(request, id):
    
    #id=request.POST["id"]
    # logging.debug(id)
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return HttpResponse("sucessfully added",content_type="text/plain")



@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart_detail.html')


