"""pimek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from store import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.index, name='index'),
    path('fetch',  views.fetch, name='fetch'),   
    path('iot',  views.iot, name='iot'),
    # path('add',  views.add, name='add'),
    # path('add_leader',  views.add_leader, name='add_leader'),
    # path('subcategory/<str:slug>',  views.subcategory, name='subcategory'),
    # path('single/<str:slug>',  views.single, name='single'),
    # path('checkout/',  views.checkout, name='checkout'),
    # path('search/',  views.search, name='search'),
    # path('/product/<int:id>/',  views.product, name='product'), 
]
