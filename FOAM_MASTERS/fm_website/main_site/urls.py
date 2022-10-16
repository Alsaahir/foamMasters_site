from django.urls import path
from . import views
# from django.views.generic import TemplateView


urlpatterns = [
   path('about/', views.about, name='about'),
   path('blog_details/', views.blog_details, name='blog_details'),
   path('blog_home/', views.blog_home, name='blog_home'),
   path('contact_us/', views.contact_us, name='contact_us'),
   path('elements/', views.elements, name='elements'),
   path('', views.index, name='index'),
   path('menu/', views.menu, name='menu'),
   path('test/', views.test, name='test'),
]