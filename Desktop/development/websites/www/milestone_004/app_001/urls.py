from django.conf.urls import url
from app_001 import views
from django.urls import include

app_name = 'app_001'

urlpatterns = [
    url(r'^$',views.index,name='index'), 
    url(r'^register/$',views.register,name='register'), 
    url(r'^user_login/$',views.user_login,name='user_login'),
]












