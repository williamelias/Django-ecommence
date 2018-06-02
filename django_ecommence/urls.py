
from django.conf.urls import url, include
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contato/$', views.contact, name="contact"),
    url(r'^$', views.index, name="index"),
    url(r'^produto/$', views.product, name="product"),
    url(r'^produtos/$', views.product_list, name="product_list"),
]
