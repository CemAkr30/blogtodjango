from django.db import models

# Create your models here.


class Article(models.Model):
    # user modeli ile ilişkilendirme yaptık ve silinmesi durumunda cascade ile silinmesini sağladık
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    # auto_now_add otomatik tarih basar
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.title
