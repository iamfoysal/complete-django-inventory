from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'category', 'created_at')
    prepopulated_fields = {'slug' : ('title',)}




admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.site_header = 'Shop Admin'