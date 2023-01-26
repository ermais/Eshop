from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])
def get_upload_to_product_image(instance,filename):
    name = instance.name 
    file_slices = filename.split(".")
    file_extension = file_slices[len(file_slices)-1]
    file_path = "prouduct/poster/%s/%s.%s" % (instance.slug,name,file_extension)
    return file_path

def get_upload_to_product_images(instance,filename):
    name = instance.product.name 
    file_slices = filename.split(".")
    file_extension = file_slices[len(file_slices)-1]
    file_path = "prouduct/images/%s/%s.%s" % (instance.product.slug,name,file_extension)
    return file_path

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to=get_upload_to_product_image, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',args=[self.id, self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_to_product_images)

    def __str__(self):
        return self.product.name




    
