#django ck editör yazarak aratıp installation yazan yere gidiyoroz dökümantasyonda terminalde "pip install django-ckeditor" yazmamız isteniyor.ck editor u indirdikten sonra setting.py de app lerin altına ekleyip tanıtalım şimdi staticfiles dosyasının altına atmak için "python manage.py collectstatic" komutunu çalıştıralım.models.py de  ckeditör dahil edelim
from audioop import reverse
from ensurepip import bootstrap
from multiprocessing import context
from typing import Reversible
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404#get_object_or_404 id miz varsa döndürecek yoksa 404 hatası fırlatacak

from article.models import Article
from.forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required#Oturum kontrolu yapabilmek çin https://docs.djangoproject.com/en/2.0/topics/auth/default/i adresinde belirtildiği gibi  login_required i dahil ediyoruz 
# Create your views here.

def articles(request):#tüm article leri gösterelim
    keyword=request.GET.get("keyword")
    if keyword:
        articles=Article.objects.filter(title__contains=keyword)#keyword ün geçtiği article leri title__contains komutuyla aratıyoruz
        return render(request,"articles.html",{"articles":articles}) 
    articles=Article.objects.all()#Bizim arama işlemimiz olmadıysa if koşoluna girmeyeceğiz tüm articles ları listeye atadık
    return render(request,"articles.html",{"articles":articles})#article leri göndereceğiz
    




def index(request):          
    context={        
        "number1":6985,
        "number2":10000,
        "numbers":["a","b","c","d","e","f"]
    }
    #return render HttpResponse("Anasayfa")
    return render(request,"index.html",context)       

def about(request):   
    return render(request,"about.html") 

def detail(request,id):    
    return HttpResponse("detail"+str(id))
    
@login_required(login_url="user:login")#dashboard den önce yazdığımız için dashboarda gitmek istediğimizde giriş yapmadığımızdabize hata verir o yüzden user altındaki login urlye gidelim    
def dashboard(request):
    articles=Article.objects.filter(author=request.user)#sisteme kim girmişse onun article lerini alalım  
    context={"articles":articles}#articles ile aldığımız article leri context diye sözlük değişkenine atadık ve render e gönderdik şimdi dashboard.html de gösterelim 
    
    return render(request,"dashboard.html",context)
    
@login_required(login_url="user:login")    
def addArticle(request):
    form=ArticleForm(request.POST or None,request.FILES or None)
  
    if form.is_valid():
        article=form.save(commit=False)#form tabanlı çalıştığımız için direk kaydedebiliriz (commit=False) article objesini oluştur kayıt işlemini yapma diyoruz.aksi takdirde yazar bilgisi ve id olmadığı için django hata verir 
        article.author=request.user
        article.image=request.user
        article.save()
        messages.success(request,"Makale Başarıyla oluşturuldu")
        return redirect("index")
    
    
    return render(request,"addarticle.html",{"form":form})

@login_required(login_url="user:login")    
def detail(request,id):
    #article=Article.objects.filter(id=id).first() gördüğü ilk article çalıştır
    article=get_object_or_404(Article,id=id)#id si olan sayfayı görüntülemek istersek(sayfa varsa) sayfa görünecek yoksa 404 hatası verecek
    comments=article.comments.all()#models.py de oluşan article içindeki comment leri alıp "comments":comments şeklinde temlates a gönder

    
    
    return render(request,"detail.html",{"article":article,"comments":comments})
@login_required(login_url="user:login")  
def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article)#instance ile posttan gelen bilgiler formun içine yazılacaktır

    if form.is_valid():
        article=form.save(commit=False)#form tabanlı çalıştığımız için direk kaydedebiliriz (commit=False) article objesini oluştur kayıt işlemini yapma diyoruz.aksi takdirde yazar bilgisi ve id olmadığı için django hata verir 
        
        article.author=request.user
        article.save()
        messages.success(request,"Makale Başarıyla güncellendi")
        return redirect("index")
    
    
    return render(request,"update.html",{"form":form})
    
    
@login_required(login_url="user:login")    
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)

    article.delete()
    messages.success(request,"Makale Başarıyla Silindi")
    
    return redirect("article:dashboard")   #article uygulaması altındaki dashboarda git
@login_required(login_url="user:login")    
def addComment(request,id):
    article=get_object_or_404(Article,id=id)
    if request.method=="POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
    
    
        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article    
        newComment.save()
    
    return redirect(reverse("article:detail",kwargs={"id":id}))
