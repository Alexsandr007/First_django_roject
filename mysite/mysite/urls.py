"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contact/',include('email_contact.urls',namespace='contact')),
    path('contact/<int:post_id>',views.contact_page_post,name='contact_post'),
    path('cars/',include('cars.urls',namespace='cars')),
    path('',views.home_page,name='home'),
    path('about/',views.about_page,name='about'),
    path('services/',views.services_page,name='services'),
    path('pricing/',views.pricing_page,name='pricing'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)