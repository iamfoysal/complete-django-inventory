from django.urls import path

from . import views

# Inventory Routing

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.productlist_api, name='product-list'),
    path('api/add/', views.add_product_api, name='product-add'),
    path('api/detail/<str:pk>/', views.detail_product_api, name='product-detail'),
    path('api/update/<str:pk>/', views.update_product_api, name='product-update'),
    path('api/delete/<str:pk>/', views.delete_product_api, name='product-delete'),

    #general view
    path('add-product/', views.add_product, name='add-product'),
    path('edit-product/<str:pk>/', views.edit_product, name='edit-product'),
    path('delete-product/<str:pk>/', views.delete_product, name='delete-product'),
    path('category/<str:pk>/', views.category_product, name='category-product'),
    path('product/details/<str:pk>/', views.detail_product, name='details-product'),
]
