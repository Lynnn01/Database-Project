from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth, login as alogin, logout as alogout
from userapp.models import Userinfo

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        phone = request.POST["phone"]
        message = ""
        if (
            username == ""
            or email == ""
            or password == ""
            or firstname == ""
            or lastname == ""
            or phone == ""
        ):
            messages.warning(request, "กรุณาป้อนข้อมูลให้ครบ")
            return redirect("/register")
        else:
            if User.objects.filter(username=username).exists():
                message = "ชื่อผู้ใช้"

            elif User.objects.filter(email=email).exists():
                message = "อีเมล"

            elif Userinfo.objects.filter(phone=phone).exists():
                message = "เบอร์โทร"
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()

                user_info = Userinfo.objects.create(member=user, phone=phone, point=0)
                user_info.save()
                messages.success(request, "สร้างบัญชีผู้ใช้เรียบร้อย")
                return redirect("/login")

            if message != "":
                messages.warning(request, f"{message}ถูกใช้งานแล้ว")
                return redirect("/register")
    else:
        return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "" or password == "":
            messages.warning(request, "กรุณาป้อนข้อมูลให้ครบ")
            return redirect("/login")

        else:
            user = auth(request, username=username, password=password)

            if user is not None:
                alogin(request, user)
                return redirect("/")
            else:
                messages.warning(request, "ไม่พบข้อมูลผู้ใช้")
                return redirect("/login")

            # try:
            #     password_auth = User.objects.get(username=username)

            #     if password != password_auth.password:
            #         messages.warning(request, "รหัสผ่านหรือชื่อผู้ใช้งานไม่ถูกต้อง")
            #         return redirect("/login")

            # except User.DoesNotExist:
            #     messages.warning(request, "รหัสผ่านหรือชื่อผู้ใช้งานไม่ถูกต้อง")
            #     return redirect("/login")

    else:
        return render(request, "login.html")


def logout(request):
    alogout(request)
    return redirect("/login")


def points(request, price):
    user = request.user
    points = Userinfo.objects.get(member=user)
    discount = 0

    if points.point >= 100:
        discount = points.point // 10
        points.point = 0
        points.save()

    points.point += (price - discount) // 10
    points.save()

    return discount
