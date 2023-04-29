from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User  # user modeli için import ettik
from django.contrib.auth import login as auth_login, authenticate as auth_authenticate, logout as auth_logout
from django.contrib import messages
# Create your views here.


def register(request):
    if (request.method == "POST"):
        # formdan gelen verileri alıyoruz yani client tarafından modellere doldurulan verileri nesnelere setliyoruz
        form = RegisterForm(request.POST)
        if (form.is_valid()):  # formun geçerli olup olmadığını kontrol ediyoruz misal clean fonksiyonu içindeki şartları kontrol ediyoruz
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # user modeline göre bir nesne oluşturuyoruz
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()  # veritabanına kaydediyoruz yani modeli kaydediyoruz nesneler üzerinde işlemi yaptık ve kaydettik ORM ile

            # login işlemi için
            # sisteme giriş yaptırdık ve kullanıcıyı sisteme kaydettik yani aslında flask da ki session işlemini yaptık
            auth_login(request, newUser)
            messages.success(request, "Başarıyla Kayıt Oldunuz")
            # index sayfasına yönlendiriyoruz
            return redirect("index")
        else:
            form = RegisterForm()
            context = {
                "form": form
            }
            return render(request, "article/register.html", context)
    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "article/register.html", context)


def login(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if (form.is_valid()):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        # authenticate fonksiyonu ile kullanıcıyı doğruluyoruz yani veritabanında var mı yok mu diye kontrol ediyoruz
        user = auth_authenticate(request, username=username, password=password)

        if (user is None):
            messages.warning(request, "Kullanıcı Adı veya Parola Hatalı")
            return render(request, "article/login.html", context)

        messages.success(request, "Başarıyla Giriş Yaptınız")
        # kullanıcıyı sisteme kaydettik yani aslında flask da ki session işlemini yaptık
        auth_login(request, user)  # CemAkr30 Akar1905gs
        return redirect("index")

    else:
        return render(request, "article/login.html", context)


def logout(request):
    auth_logout(request)
    messages.success(request, "Başarıyla Çıkış Yaptınız")
    return redirect("index")
