
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from MyApp1 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^poo/',views.view1)
]
