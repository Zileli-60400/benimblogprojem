
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):#django dökümantasyonda model formlar kullanılışlı bunları kullanabiliriz   
    class Meta:
        model = Article#modelimizle formumuz Article bağlantılı hale geldi.modelimizde(models.py) hangi alanlar varsa ona göre alanlar oluşturacak
        fields=["title","content","article_image"]#title ve content alanına giriş yaparak form oluştur dedik.article_image ekleyerek fotoğraf ekleme bağlantısını oluşturduk
  
