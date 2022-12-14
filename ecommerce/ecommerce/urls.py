"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from contable.views import inicio, contabilidad, ejercicio, crearejercicio, libromayor, crearmayor, detmayor, diario, creardiario, detdiario, articulo, cliente, crearCliente, venta
from django.conf.urls.static import static
from ecommerce import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('contabilidad/', contabilidad, name='contabilidad'),
    path('ejercicio/', ejercicio, name='ejercicio'),
    path('crearejercicio/', crearejercicio, name='crearejercicio'),
    path('libromayor/', libromayor, name='libromayor'),
    path('crearmayor/', crearmayor, name='crearmayor'),
    path('detmayor/', detmayor, name='detmayor'),
    path('diario/', diario, name='diario'),
    path('creardiario/', creardiario, name='crearDiario'),
    path('detdiario/', detdiario, name='detDiario'),
    path('articulo/', articulo, name='articulo'),
    path('cliente/', cliente, name='cliente'),
    path('crearcliente/', crearCliente, name='crearcliente'),
    path('venta/', venta, name='venta'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)