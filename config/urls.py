
from django.urls import path
from . import views


urlpatterns = [
    path("config/", views.course_list_api, name="config"),

]
