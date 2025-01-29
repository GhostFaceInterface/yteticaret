from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Kategoriler(models.Model):
    isim=models.CharField(max_length=155)
    ustkategori=models.ForeignKey('self',on_delete=models.CASCADE ,null=True,blank=True, help_text="Üst Kategori")
    aktifmi=models.BooleanField(default=True)
    seo_title=models.CharField(max_length=155,null=True,blank=True)
    seo_description=models.TextField(null=True,blank=True)
    slug=models.SlugField(max_length=155,unique=True, null=True,blank=True)  

    class Meta:
        verbose_name_plural="Kategoriler"
        verbose_name="Kategori"

    def __str__(self):  
        return self.isim

class Markalar(models.Model):
    isim=models.CharField(max_length=155)
    aciklama=models.TextField(blank=True,null=True)
    seo_title=models.CharField(max_length=155,null=True,blank=True)
    seo_description=models.TextField(null=True,blank=True)
    slug=models.SlugField(max_length=155,unique=True, null=True,blank=True)
    aktifmi=models.BooleanField(default=True)
    resim=models.ImageField(upload_to='markaresimleri',null=True,blank=True)

    class Meta:
        verbose_name_plural="Markalar"
        verbose_name="Marka"

    def __str__(self):  
        return self.isim

class Etiketler(models.Model):
    isim=models.CharField(max_length=155)
    slug=models.SlugField(max_length=155,unique=True, null=True,blank=True)
    aktifmi=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural="Etiketler"
        verbose_name="Etiket"

    def __str__(self):  
        return self.isim        

class Urunler(models.Model):
    isim=models.CharField(max_length=50)
    kullanici=models.ForeignKey(User,on_delete=models.CASCADE)
    fiyat=models.DecimalField(max_digits=10,decimal_places=2)
    kategori=models.ForeignKey(Kategoriler,on_delete=models.CASCADE)
    marka=models.ForeignKey(Markalar,on_delete=models.CASCADE)
    indirimli_fiyat=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    kisa_aciklama=models.TextField(null=True,blank=True)
    aciklama=models.TextField(null=True,blank=True)
    seo_title=models.CharField(max_length=155,null=True,blank=True)
    seo_description=models.TextField(null=True,blank=True)
    slug=models.SlugField(max_length=155,unique=True, null=True,blank=True)
    aktifmi=models.BooleanField(default=True)
    resim=models.ImageField(upload_to='urunresimleri',null=True,blank=True)
    tarih=models.DateTimeField(auto_now_add=True)
    etiketler=models.ManyToManyField(Etiketler, blank=True)
    anasayfa=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="Ürünler"
        verbose_name="Ürün"

    def __str__(self):  
        return self.isim
