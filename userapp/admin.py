from django.contrib import admin
from userapp.models import Userinfo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserInline(admin.StackedInline):
    model = Userinfo
    can_delete = False
    verbose_name_plural = "user"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserInline]
    # list_display = [
    #     "username",
    #     "email",
    #     "first_name",
    #     "last_name",
    # ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register your models here.


# @admin.register(Userinfo)
# class manageUser(admin.ModelAdmin):
#     list_display = ["member", "phone", "point"]
#     search_fields = ("member__username",)
