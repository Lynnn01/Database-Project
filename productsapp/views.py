from django.shortcuts import render
from productsapp.models import *
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    products = Product.objects.filter(isTrending=True)
    return render(
        request,
        "index.html",
        {"products": products},
    )


def productDetail(request, id):
    product_detail = Product.objects.get(id=id)
    return render(
        request,
        "detail.html",
        {"details": product_detail},
    )


def products(
    request,
):
    products = Product.objects.all().order_by("name")
    # หมายเลขหน้า
    page = request.GET.get("page")
    paginator = Paginator(products, 3)

    products = paginator.get_page(page)

    return render(request, "product.html", {"products": products})
