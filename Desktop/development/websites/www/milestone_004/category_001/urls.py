from django.conf.urls import url, include
from .views import all_images

urlpatterns = [
    url(r'^$', all_images, name='category_001'),
]