from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from data.urls import routeur as root
routeur = routers.DefaultRouter()
routeur.registry.extend(root.registry)

urlpatterns = [
    path('', include(routeur.urls), name="home"),
    path('admin/', admin.site.urls),
]
