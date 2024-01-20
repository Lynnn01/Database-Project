from django.contrib import admin
from userapp.models import Point

# Register your models here.


@admin.register(Point)
class managePoint(admin.ModelAdmin):
    list_display = ["member", "point"]
    search_fields = ("member__username",)
