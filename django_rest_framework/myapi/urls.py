from django.urls import path, include
from myapi import views


urlpatterns = [
    path('', views.StudentCreateddisplay.as_view()),
    path('student/<int:pk>', views.StudentUpdatedelete.as_view()),

]
