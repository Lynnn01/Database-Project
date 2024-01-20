from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cartapp.models import Cart, cartItem
from orderapp.models import Order, OrderDetail
from productsapp.models import Product
from cartapp.views import create_cartId
from tablesapp.models import Table
from userapp.views import points

# Create your views here.


@login_required(login_url="/login")
def order(request):
    user = request.user

    if request.method == "POST":
        duration = request.POST["duration"]
        quantity = request.POST["quantity"]

        table = Table.objects.get(customer=user)
        cart = Cart.objects.get(cart_id=create_cartId(request), customer=user)
        item = cartItem.objects.get(cart=cart)

        total = float(item.product.price) * float(int(duration))

        discount = (points(request, total))

        order = Order.objects.create(
            duration=duration,
            quantity=quantity,
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
    order = Order.objects.filter(customer=user)
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
