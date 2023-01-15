from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView
from . serializers import courseSerializer
from .models import Course
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET',  'POST', 'DELETE', 'PUT'])
def course_list_api(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        print(courses)
        serializer = courseSerializer(courses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = courseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        courses = Course.objects.all()
        courses.delete()
        return Response("All courses deleted")
    elif request.method == 'PUT':
        courses = Course.objects.all()
        courses.delete()
        serializer = courseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    courses = Course.objects.all()

   