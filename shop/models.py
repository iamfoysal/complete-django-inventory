import uuid

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null = False, blank =False)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural= 'Categories' 

class Product(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    stock = models.IntegerField(default=0, null=True, blank=True)
    description= models.TextField(max_length=500, null = False, blank =False)
    image = models.ImageField(upload_to='images/product/', default= 'images/notfound.png', null=True, blank=True,) 
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural= 'Products' 
        
  