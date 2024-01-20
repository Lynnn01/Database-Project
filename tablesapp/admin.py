from django.contrib import admin
from tablesapp.models import *

# Register your models here.


@admin.register(Table)
class ManageSeat(admin.ModelAdmin):
    list_display = ["name", "slot", "status", "customer"]
    list_editable = ["slot", "status","customer"]
    search_fields = ["name", "customer__username"]
    list_filter = ["status"]
