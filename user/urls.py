from user import views
from django.urls import path

# article uygulamasındaki views.py içindeki index fonksiyonunu import ettik

# include ile bu uygulamaya ait url lerin başına article/ eklemek için
app_name = "user"


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
