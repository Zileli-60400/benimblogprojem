#python manage.py shell komutuyla django shell ekranın açtım komutları buraya yazalım
#Django nun sogularını orm sorgularını gerçekleştirebiliriz
#şimdi django için user tablosunu user modelini almak istiyorum (from django.contrib.auth.models import User ) uygulaması içinden user tablosunu
#"from article.models import Article" komutuyla daha önce oluşturduğum Article modelini dahil ediyorum
#user tablosundan,modelinden kullanıcı ve şifre olan obje oluşturacağız.  newUser=User(username="Denemekullanici",password="12345")
#newUser.save() komutuyla veritabanına kaydettik ama parola şifrelenmemiş görüküyor
#newUser2=User(username="denemekullanici2") komutuyla yeni kullanıcı oluşturduk şimdi şifrelemek için newUser2.set_password("12345") komutunu yazıp newUser2.save() ile kaydedelim
#newUser3=User() şeklinde obje oluşturup useri boş bırakalım
#newUser3.username="deneme kullanici3" komutuyla username oluşturduk
#newUser3.set_password("12345") ve newUser3.first_name="Abdullah Bey" komutları ile tanımlamalar yapıldı
#newUser.save() komutuyla veritabanına kaydettik
#article oluşturalım 'article=Article(title="django shell deneme",content="içerik içerik",author=newUser3)' komutunda title,content tanımlandı sonunda autherini newUser3 e atadık
#article.save() ile kaydedelim
#article i 'article=Article.objects.create(title="Deneme21",content="58",author=newUser2)' şeklindede oluşturabiliriz
# Article.objects.all() ile bütün article lar alınır;Article.objects.get(title="Deneme Makalesi") ile title ı deneme makalesi olan alınır
#article.delete() ile article veri tabanından silinir.
#veritabınında sorgulama için title__contains sorgusu çalıştırılır(Article.objects.filter(title__contains="Den")) yani title in içinde Den geçenleri al
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from article import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('detail/<int:id>',views.detail,name="detail"), #detail şeklinde bir foksiyon tanımlayacağız int olan bir id ye gidecek ve bir dinamik id olacak adres çubuğunda detail/1 veya detail/2 ye gidebilecek
    
    path('articles/',include("article.urls")),#article içindeki urls e bağladık http://localhost:8000/articles/create/ adresine gidince anasayfaya gidiyoruz
    path('user/',include("user.urls")),
  
]    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
    
    
        
