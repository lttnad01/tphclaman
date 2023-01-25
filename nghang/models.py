from tabnanny import verbose
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
CATEGORY_CHOICES = (
    ('banchay','Bán chạy'),
    ('moive','Mới về'),
)
ADS_CHOICES =(
  ('chon', 'Chọn'),
  ('khongchon', 'Không Chọn')
)

class Nghang(models.Model):
  ngname = models.CharField(max_length=100, verbose_name='Tên ngành hàng')
  ngicon = models.ImageField(upload_to='icon/',verbose_name='Icon')
  class Meta:     
    verbose_name = 'Ngành hàng'
    verbose_name_plural = 'Ngành hàng'
  def __str__(self):
        return str(self.ngname)

class Product(models.Model):
  prname = models.CharField(max_length=100, verbose_name='Tên sản phẩm')
  price = models.IntegerField(blank=True, null=True, verbose_name='Giá tiền') 
  prcontent= models.TextField(verbose_name="Nội dung")
  primage = models.ImageField(upload_to='imgProduct/',verbose_name='Ảnh sản phẩm')
  slug = models.SlugField(blank=True, null=True, verbose_name='Tên đường dẫn')
  nghang=models.ForeignKey(Nghang, related_name='lk_nghang',on_delete=models.CASCADE, verbose_name='Ngành hàng' )
  category = models.CharField(blank=True, null= True,choices=CATEGORY_CHOICES , max_length=10)
  def save(self , *args , **kwargs):
      if not self.slug :
            self.slug = slugify(self.prname)
        
      super(Product, self).save( *args , **kwargs)
  class Meta:     
    verbose_name = 'Sản phẩm'
    verbose_name_plural = 'Sản phẩm'
 
  def __str__(self):
        return str(self.prname) + str(self.price)
        

class Intro(models.Model):
  incontent= models.TextField(verbose_name="Nội dung giới thiệu")
  phone = models.CharField(max_length=20, verbose_name='Số điện thoại')
  address = models.CharField(max_length=100, verbose_name='Địa chỉ')
  mymap= models.CharField(max_length=500, verbose_name='Google Map')
  
  class Meta:     
    verbose_name = 'Giới Thiệu'
    verbose_name_plural = 'Giới Thiệu'
  def __str__(self):
    return 'Chỉnh sửa'

class ProductImage(models.Model):
  imgname= models.ImageField(upload_to='imgProduct/',verbose_name='Ảnh chi tiết sản phẩm')
  productID=models.ForeignKey(Product, related_name='lk_product',on_delete=models.CASCADE, verbose_name='Sản phẩm' )
  class Meta:     
    verbose_name = 'Ảnh chi tiết sản phẩm'
    verbose_name_plural = 'Ảnh chi tiết sản phẩm'
  def __str__(self):
    return str(self.imgname)

class News(models.Model):
  postname= models.CharField(max_length=200,verbose_name='Tiêu đề bài viết')
  postcontent= models.TextField(verbose_name="Nội dung bài viết")
  date= models.DateField(verbose_name="Thời gian")
  postimage=models.ImageField(blank=True, null=True,upload_to='imgPost/',verbose_name='Ảnh bài viết')
  slug = models.SlugField(blank=True, null=True, verbose_name='Tên đường dẫn')
  ads = models.CharField(blank=True, null= True,choices=ADS_CHOICES , max_length=10, verbose_name='Chọn làm quảng cáo')
  def save(self , *args , **kwargs):
      if not self.slug :
            self.slug = slugify(self.postname)
        
      super(News, self).save( *args , **kwargs)

  class Meta:     
    verbose_name = 'Tin tức'
    verbose_name_plural = 'Tin tức'
  def __str__(self):
    return str(self.postname)