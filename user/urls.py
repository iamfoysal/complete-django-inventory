from django.urls import path
from . import views

# user Routing

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('signout/', views.signout, name='signout'),
   
   
]