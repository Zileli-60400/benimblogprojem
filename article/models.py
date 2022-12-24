from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField 
from django.conf.urls.static import static
# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")#user tablosunu işaret etmek için foreignkey diyoruz ve on_delete komutu userimiz yani kullanıcı silinirse kullanıcının oluşturduğu verilerde silinsin amacıyla kullanılıyor verbose_name="Yazar" komutu başlığı yazar olarak değiştiriyor
    title=models.CharField(max_length=50,verbose_name="Başlık")
    content=RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")#o anki tarihi otomatik ekleyecek şimdi admin paneline admin.py dosyasında ekleyelim
    article_image= models.FileField(blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekleyin")#model değiştiği için terminalde  python manage.py makemigrations komutuyla django ya söylemeliyiz veritabanına işlemek içinde  python manage.py migrate komutunu yazalım
    def __str__(self):#bu fonksiyonla panelde başlık görünsün istiyorsak title,yazarı istiyorsak author şeklinde gösteririz
        return self.title


    class Meta():#makaleleri tarihe göre sıralamak için Meta clasını kullanalım django daki meta ordering e bakalım
       ordering=['-created_date'] #başına "-" koyduğumuzda en son eklenen makale ilk önce gösterilir ve model değiştiği için djanya komut isteminde makemigrations  komutuyla söyleyip migrate ile veri tabanına kaydedelim.   
        

class Comment(models.Model):#Makaleye yorum özelliği eklemek için herbir makalemin postları olacak o yüzden comment class ı oluşturalım 
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")#herbir article in bir çok commenti olabilir ForeignKey yardımıyla commentlerimizi buradaki article lere bağlayacağız.related_name i comments diye isimlendirirsek ilerde bir article aldığımızda article.comments dediğimizde comments tablosuna erişebilirim.
    comment_author=models.CharField(max_length=50,verbose_name="İsim")
    comment_content=models.CharField(max_length=200,verbose_name="Yorum")   
    comment_date=models.DateTimeField(auto_now_add=True)#Yorum yapacak isim konu ekledik şimdi admin panelinde göstermek için admin.py de gösterelim    
    def __str__(self):   
        return self.comment_content
    class Meta():    
        ordering=['-comment_date']
