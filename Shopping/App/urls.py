from django.conf.urls import url

from App import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^detail/$',views.detail,name='detail'),
    url(r'^shopping_car/$', views.shopping_car, name='shopping_car'),
]