from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


class StudentCreateddisplay(generics.ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdatedelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
