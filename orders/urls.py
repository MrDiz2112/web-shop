from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.OrderCreate, name='OrderCreate'),
    url(r'^created/$', views.OrderCreated, name='OrderCreated')
]