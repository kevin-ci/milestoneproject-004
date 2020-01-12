"""milestone_004 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from app_001 import views

from products import urls as urls_products
from products.views import all_products

from cart import urls as urls_cart

from category_001 import urls as urls_category_001
from category_001.views import all_images

from django.views import static
from .settings import MEDIA_ROOT



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$',views.index,name='index'),

    url(r'^app_001/', include('app_001.urls')),

    url(r'^products/', include('products.urls')),

    url(r'^category_001/', include('category_001.urls')),

    url(r'^cart/', include('cart.urls')),
    
    url(r'^logout/$',views.user_logout,name='logout'),

    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
   
]
