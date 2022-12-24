from django.contrib import admin
from .models import Article,Comment 
# Register your models here.

admin.site.register(Comment)#commenti gösterdik şimdi modelimizi database göstermek için terminalde python manage.py makemigrations komutuyla(article\migrations\0004_comment.py) model oluşturmuş olduk.şimdi python manage.py migrate komutuyla veritabanında comment tablosu oluşturalım(Applying article.0004_comment... OK)


#admin.site.register(Article)#Article modelini dahil ettik ancak django bildirmedik bunu settings.py deki app ye ekleyerek app mimizi bildirelim("article",)
@admin.register(Article)#Biz admin paneline decarator olarak yazmak istiyorum
class ArticleAdmin(admin.ModelAdmin):#admin panelini özelleştireceğimiz bir class oluşturdum ve bu class ModelAdmin den türeyecek
    
    class Meta:#ArticleAdmin admin classı Article modelini özelleştireceğini söylemeliyiz bunu django da olan Meta classı ile söyleyip ikisi birleştirilyor
        model=Article

    list_display=["title","author","content","created_date"]#Artık admin panelinde yazar bilgiside görünüyor
    list_display_links=["title","created_date","content"]#başlık,tarih ve içeriğe link eklendi basınca aynı makale sayfasına gidiyor.Djangodocumantasyon dan diğer özellikler bulunabilir
    search_fields=["title"]#başlığa göre admin panelindeki makaleleri arayabiliriz
    list_filter=["created_date"]#makalelerin oluşturulduğu tarih,title yazarsak başlıkları süzer
