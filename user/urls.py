#Terminalde "python manage.py startapp user" komutuyla user adında uygulama oluşturdum.ve burada urls.py dosyası oluşturdum article uygulamamda olan urls.py dosyasındaki modulleri alalım   

from django.contrib import admin
from django.urls import path
from . import views

app_name="user"
urlpatterns = [
    path('register/', views.register,name="register"),#register url si geldiğinde views.index çalışacak
    path('login/', views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
]    
#şimdi uygulama içindeki views.py de fonksiyonları yazalım 
#Şimdi ana dosya(blog/urls.py)'ya  user/user.urls i gösterelim. komut="path('user/',include("user.urls")),"
 #Django yada söylememiz gerekiyor.Bunun için blog içindeki settings.py ye INSTALLED_APPS bölümü sonunda 'user' şeklinde ekleyelim  
#Şimdi form clasımı oluşturmak için user içinde forms.py adında dosya oluşturalım 
