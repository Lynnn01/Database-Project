from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from productsapp.models import Product
from cartapp.models import Cart, cartItem
from tablesapp.models import Table

# Create your views here.


def create_cartId(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


@login_required(login_url="/login")
def cart(request):
    user = request.user
    counter = 0
    total = 0

    try:
        cart = Cart.objects.get(cart_id=create_cartId(request), customer=user)
        emptyCart(request, cart)
        item = cartItem.objects.filter(cart=cart)
        for i in item:
            counter += i.quantity
            total += i.quantity * i.product.price
    except (Cart.DoesNotExist, cartItem.DoesNotExist):
        cart = None
        item = None

    if cartItem.objects.filter(cart=cart).exists() == False:
        return render(request, "empty.html")
    return render(
        request, "cart.html", {"item": item, "counter": counter, "total": total}
    )


@login_required(login_url="/login")
def addCart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user = request.user

    if Table.objects.filter(customer=user).exists():
        # create a new cart
        try:
            # have a cart
            cart = Cart.objects.get(cart_id=create_cartId(request))
        except Cart.DoesNotExist:
            # haven't a cart
            cart = Cart.objects.create(cart_id=create_cartId(request), customer=user)
            cart.save()

        item_reset = cartItem.objects.filter(cart=cart)
        item_reset.delete()
        item = cartItem.objects.create(product=product, cart=cart, quantity=1)
        item.save()

        return redirect("/cart")

    else:
        messages.warning(request, "โปรดจองโต๊ะก่อนเลือกบอร์ดเกม")
        return redirect("/tables")


def emptyCart(request, cart):
    if cartItem.objects.filter(cart=cart) is None:
        return render(request, "emptyCart.html")


@login_required(login_url="/login")
def removeCart(request, product_id):
    user = request.user
    cart = Cart.objects.get(cart_id=create_cartId(request), customer=user)
    product = Product.objects.get(pk=product_id)
    item = cartItem.objects.get(product=product, cart=cart)
    item.delete()

    # product = Product.objects.get(pk=product_id)
    # cart = Cart.objects.get(customer=user)
    # item = cartItem.objects.get(product=product, cart=cart)

    # if item.quantity - 1 > 0:
    #     item.quantity -= 1
    #     item.save()
    # else:
    #     item.delete()
    emptyCart(request, cart)
    return redirect("/cart")
    pass
