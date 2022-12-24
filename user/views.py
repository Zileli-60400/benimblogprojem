from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
# Create your views here.
from django.contrib.auth.models import User#user modelini dahil ettik
from django.contrib.auth import login,authenticate,logout #login olmak için yani sisteme dahil olmak için login fonksiyonunu dahil ettik. authenticate fonksiyonu bizim username kullanıcıya göre kullanıcı olup olmadığını sorgular
from django.contrib import messages#"docs.djangoproject.com/en/4.1/ref/contrib/messages/" adresinde anlatıldığı gibi django mesajlarını import ettik 
def register(request):#Kayıt formundaki bilgileri alacak
    form=RegisterForm(request.POST or None)#formumuz post request olduysa form doldurulacak get request olduysa none olarak yani boş oluşacak bir şey göndermeyecek
    if form.is_valid(): 
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        newUser=User(username=username)
        newUser.set_password(password)#parola şifrelendi

        newUser.save()#kullanıcı veritabanına kaydedilecek
        login(request,newUser)#Hem kayıt oldu hemde sisteme girmiş oldu 
        messages.success(request,"Başarıyla Kayıt Oldunuz.......")#success olunca yeşil,warning olsa sarı arka planlı mesaj yayınlanır.diğer türlere django doc tan bakabiliriz bir mesaj bir kere yayınlanır 
        
        
        return redirect("index")
        
    context={"form":form}#post request olduğu ve is_valid olmamışsa bilgileri girmeyecek 
        
    return render(request,"register.html",context)      
"""    
    BU BÖLÜMDE FARKLI YÖNTEMLE FORM GİRİŞ OLUŞTURULDU
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():#post request gönderildiğinde is_valid metoduyla forms.py deki clean metodu çağrılacak artık dataları alabiliriz. 
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            newUser=User(username=username)
            newUser.set_password(password)#parola şifrelendi

            newUser.save()#kullanıcı veritabanına kaydedilecek
            login(request,newUser)#Hem kayıt oldu hemde sisteme girmiş oldu 
            return redirect("index")#blog projesinde urls.py de name i index demiştik "path('',views.index,name="index")," redirect işlemiyle django işlemi gerçekleştirecek
        context={"form":form}
        
        return render(request,"register.html",context)    
    else:    
        form=RegisterForm()    
        context={"form":form}
        
        return render(request,"register.html",context)
    
    #form=RegisterForm()
    #context={"form":form}
    #return render(request,"register.html",context)"""
                                                   
def loginUser(request):#Giriş işlemi gerçekleştirilecek
    form=LoginForm(request.POST or None)
    
    context={"form":form}
    if form.is_valid(): 
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user=authenticate(username=username,password=password)#username ve password u authenticate ile kontrol ederiz ve user değişkenine atadık
    
        if user is None:#kullanıcı adı veya password yoksa
            messages.info(request,"Kullanıcı Adı veya parola hatalı ")
            return render(request,"login.html",context)#
            
        messages.success(request,"Başarıyla giriş yaptınız")#form valid olduysa mesaj yayınlandı
        login(request,user)#Hem kayıt oldu hemde sisteme girmiş oldu
        return redirect("index")
            
    return render(request,"login.html",context)#get request yaptıysa login sayfasına yani form sayfasına gidecek

def logoutUser(request):#Çıkış işlemi gerçekleştirilecek
    logout(request)
    messages.success(request,"Başarıyla çıkış Yaptınız..............")
    return redirect("index")
