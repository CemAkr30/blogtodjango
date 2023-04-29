from django.contrib import admin

# Register your models here.
from .models import Article

# admin.site.register(Article)  # modeli dahil ediyoruz admin panelinde


# admin register decorator ile admin panelindeki özellikleri tanımladık
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):  # admin panelindeki özellikleri tanımladık

    # listeleme özelliği tanımladık ve içine hangi özellikleri yazarsak onları listeler
    list_display = ["title", "author", "content", "created_date"]

    # hangi özelliklere tıklayarak ulaşmak istiyorsak onları tanımladık
    list_display_links = ["title", "content"]

    # hangi özelliklerin aranmasını istiyorsak onları tanımladık
    search_fields = ["title"]

    # hangi özelliklere göre filtreleme yapmak istiyorsak onları tanımladık
    list_filter = ["created_date"]  # süzgeç özelliği tanımladık

    class Meta():  # python tarafından tanımlanmış bir class olup içindeki özelliklerin hepsi python tarafından tanımlanmış özelliklerdir
        model = Article
