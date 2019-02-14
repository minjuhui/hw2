from django.contrib import admin
from django.urls import path
#import blog.views
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),  
    path('new/', views.new, name='new'),
    path('<int:blog_id>/', views.detail, name='detail'),
    
]