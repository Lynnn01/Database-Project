from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cartapp.models import Cart, cartItem
from orderapp.models import Order, OrderDetail
from productsapp.models import Product
from userapp import urls
from cartapp.views import create_cartId
from tablesapp.models import Table
from userapp.views import points
from datetime import datetime, timezone, timedelta

# Create your views here.


@login_required(login_url="/login")
def order(request):
    user = request.user

    if request.method == "POST":
        duration = request.POST["duration"]

        table = Table.objects.get(customer=user)
        cart = Cart.objects.get(cart_id=create_cartId(request), customer=user)
        item = cartItem.objects.get(cart=cart)
        receipt_number = str(
            datetime.now(timezone(timedelta(hours=+7))).strftime("%y%m%d%f")
        ) + str(user.id)

        total = float(item.product.price) * float(int(duration))

        discount = points(request, total)

        order = Order.objects.create(
            receipt_number=receipt_number,
            duration=duration,
            total=total - discount,
            customer=user,
            table=table,
        )
        order.save()

        order_detail = OrderDetail.objects.create(
            product=item.product.name,
            price=item.product.price,
            order=order,
            discount=discount,
        )
        order_detail.save()

        product = Product.objects.get(pk=item.product.id)
        product.stock = int(item.product.stock - 1)
        product.save()
        item.delete()
        cart.delete()

        return render(request, "ordercomplete.html")

    else:
        return render(request, "order.html")


@login_required(login_url="/login")
def orderHistory(request):
    user = request.user
    order = Order.objects.filter(customer=user).order_by("-id")
    if order.exists():
        return render(request, "orderhistory.html", {"order": order})

    else:
        return render(request, "orderhistory-empty.html")


@login_required(login_url="/login")
def orderDetail(request, order_id):
    user = request.user
    order = Order.objects.get(pk=order_id, customer=user)
    item = OrderDetail.objects.get(order=order)

    return render(request, "orderdetails.html", {"order": order, "item": item})


@login_required(login_url="/login")
def orderStatus(request, order_id):
    user = request.user
    order = Order.objects.get(id=order_id)
    product = Product.objects.get(
        name=OrderDetail.objects.get(order=order).product,
    )
    if order.status == False:
        order.status = True
        product.stock += 1
    else:
        order.status = False
        product.stock -= 1

    order.save()
    product.save()

    return redirect("/adminmanage")
