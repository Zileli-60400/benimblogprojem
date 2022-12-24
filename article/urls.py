from django.contrib import admin
from django.urls import path
from . import views # views içindeki fonksiyonu çalıştırabilmek için views i import ettim
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  
app_name="article"
urlpatterns = [
    path('create/', views.index,name="index"),#create url si geldiğinde views.index çalışacak
    path('dashboard/', views.dashboard,name="dashboard"),
    path('addarticle/', views.addArticle,name="addarticle"),
    path('article/<int:id>', views.detail,name="detail"),#article detay sayfasına gitmek steyince id ye git ve detail.html de tanımladığım gibi id si ne ise sayfayı getir(http://localhost:8000/articles/article/1)
    path('update/<int:id>', views.updateArticle,name="update"),#update diye bir name çalışsın ve bu fonksiyonu views.py de oluşturacağım ve güncelleyeceğim
    path('delete/<int:id>', views.deleteArticle,name="delete"),
    path('', views.articles,name="articles"),
    path('comment/<int:id>', views.addComment,name="comment"),
   
]    
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
