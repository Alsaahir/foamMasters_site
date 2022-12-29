from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.views.generic import TemplateView


urlpatterns = [
   path('base/', views.base, name='base'),
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('products/', views.products, name='products'),
   path('extra_high_density/', views.extra_high_density, name='extra_high_density'),
   path('high_density/', views.high_density, name='high_density'),
   path('medium_density/', views.medium_density, name='medium_density'),
   path('high_quality/', views.high_quality, name='high_quality'),
   path('normal_quality/', views.normal_quality, name='normal_quality'),
   path('furniture/', views.furniture, name='furniture'),
   path('cusions_and_foams/', views.cusions_and_foams, name='cusions_and_foams'),
   path('contact_us/', views.contact_us, name='contact_us'),
   path('catalog', views.catalog, name="catalog"),
   path('mail/', views.mail, name="mail"),
   
   #PASSWORD RESET PATHS
   path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
   path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]