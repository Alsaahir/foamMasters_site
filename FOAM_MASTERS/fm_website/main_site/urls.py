from django.urls import path
from . import views
# from django.views.generic import TemplateView


urlpatterns = [
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('products/', views.products, name='products'),
   path('extra_high_density/', views.extra_high_density, name='extra_high_density'),

   path('blog_details/', views.blog_details, name='blog_details'),
   path('blog_home/', views.blog_home, name='blog_home'),
   path('contact_us/', views.contact_us, name='contact_us'),
   path('menu/', views.menu, name='menu'),

   path('base/', views.base, name='base'),
   path('catalog', views.catalog, name="catalog"),
   
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]