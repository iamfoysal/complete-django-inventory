from django.forms import ModelForm
from .models import Product, Category

class ProductAddForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'stock', 'category', 'description', 'image']
        
        labels = {
            "image": ""
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': '3', 'placeholder' : 'Description'})
        self.fields['category'].empty_label ="select category"
        


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

  


