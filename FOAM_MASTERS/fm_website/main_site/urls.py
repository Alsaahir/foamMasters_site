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
   path('products/', views.products, name='products'),
   path('base/', views.base, name='base'),
   path('catalog', views.catalog, name="catalog"),
   
   path('store', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]