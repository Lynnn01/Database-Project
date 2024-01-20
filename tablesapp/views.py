from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tablesapp.models import Table

# Create your views here.


@login_required(login_url="/login")
def table(request):
    table = Table.objects.all().order_by("name")
    return render(request, "table.html", {"table": table})


def reservTable(request, table_id):
    user = request.user
    if Table.objects.filter(customer=user).exists():
        messages.warning(request, "คุณมีโต๊ะที่จองไว้อยู่แล้ว")
        return redirect("/tables")
    else:
        table = Table.objects.get(id=table_id)
        table.customer = user
        table.status = True
        table.save()
        return redirect("/tables")
