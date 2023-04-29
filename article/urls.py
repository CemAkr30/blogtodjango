from article import views

from django.contrib import admin
from django.urls import path

# article uygulamasındaki views.py içindeki index fonksiyonunu import ettik

# include ile bu uygulamaya ait url lerin başına article/ eklemek için
app_name = "article"


urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("addArticle/",views.addArticle, name ="addArticle"),
    path("update/<int:id>",views.updateArticle, name ="updateArticle"),
    path("delete/<int:id>",views.deleteArticle, name ="deleteArticle"),
    path("article/<int:id>",views.detail, name ="detail")
]
