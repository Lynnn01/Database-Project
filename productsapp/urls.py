from productsapp import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("product/details/<int:id>", views.productDetail, name="productDetail"),
    path("products", views.products, name="product"),
]
