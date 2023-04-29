from django import forms
from .models import Article


class ArticleForm(forms.ModelForm): # db üzerinde oluşturduğumuz modeli form olarak django otomatik oluşturur
    class Meta():
         model = Article # db üzerinde oluşturduğumuz modeli form olarak django otomatik oluşturur
         fields = ["title","content"] # hangi alanları formda göstereceğimizi belirttik 
