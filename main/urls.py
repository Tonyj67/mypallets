from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from django . contrib . staticfiles .urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("products/", views.products, name="products"),
    path("contact/", views.contact, name="contact"),
    path('heavy-duty-grid/', views.heavy_duty_grid, name='heavy_duty_grid'),
    path('light_grid/', views.light_grid, name='light_grid'),
    path('nestable/', views.nestable, name='nestable'),
    path('light-flat/', views.light_flat, name='light_flat'),
    path('flat-top-heavyduty/', views.flat_top_heavyduty, name='flat_top_heavyduty'),
         
    

   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #staticfiles_urlpatterns
    #static settings.STATIC_URL , document_root=settings.STATIC_ROOT,


