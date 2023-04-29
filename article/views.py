from .forms import ArticleForm
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required # login olmadan makale ekleyememesi için decorator ekledik
# Create your views here.



def index(request):
    # HttpResponse("Anasayfa")
    context = {
        "number1": 10,
        "number2": 20
    }
    return render(request, "article/index.html", context=context)


@login_required(login_url = "user:login")
def dashboard(request):
    # Model üzerinden db ye erişim ve işlemler yapmak için ORM kullanıyoruz
    articles = Article.objects.filter(author=request.user) # sadece kullanıcının yazdığı makaleleri getirir
    context ={
        "articles": articles
    }
    return render(request,"article/dashboard.html",context=context)

@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None) # formdan gelen verileri alıyoruz yani client tarafından modellere doldurulan verileri nesnelere setliyoruz
    
    if form.is_valid():
        # veritabanına kaydediyoruz yani modeli kaydediyoruz nesneler üzerinde işlemi yaptık ve kaydettik ORM ile
        article =  form.save(commit=False)  # commit=False ile veritabanına kaydetmiyoruz yani modeli kaydetmiyoruz nesneler üzerinde işlemi yaptık ama kaydetmedik ORM ile
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect("index")
    else:
        context = {
            "form": form
        }
        return render(request,"article/addArticle.html",context=context)
    
@login_required(login_url = "user:login")
def updateArticle(request,id):
    article = Article.objects.filter(id=id).first() # sadece kullanıcının yazdığı makaleleri getirir
    form = ArticleForm(request.POST or None, instance=article) # formdan gelen verileri alıyoruz yani client tarafından modellere doldurulan verileri nesnelere setliyoruz
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("index")
    else:
        context = {
            "form": form
        }
        return render(request,"article/update.html",context=context)
    
@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article = Article.objects.filter(id=id).first() # sadece kullanıcının yazdığı makaleleri getirir
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi")
    return redirect("index")


def article (request):
    pass 

def about(request):
    return render(request, "article/about.html")


def detail(request, id):
    article = Article.objects.filter(id=id).first() # sadece kullanıcının yazdığı makaleleri getirir
    return render(request, "article/detail.html", {"article": article})
