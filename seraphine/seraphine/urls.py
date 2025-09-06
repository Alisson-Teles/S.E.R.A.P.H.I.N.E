# Esse arquivo é o gerenciador de todas as rotas URL, de todos os apps, do projeto. By: CalebeS
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
