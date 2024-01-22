from django.urls import path
from tablesapp import views

urlpatterns = [
    path("tables", views.table),
    path("table/<int:table_id>", views.reservTable, name="reservTable"),
    path("table/cancel/<int:table_id>", views.cancelTable, name="cancelTable"),
]
