"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import url
from shop import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Index.as_view(), name="index"),
    #  path("update/<pk>/<int:number>", views.Update.as_view(), name="update"),
    #  url(r'^update/(?P<pk>\d+)/(?P<number>\d+)/$', views.Update.as_view(), name="update"),
    url(r'^update/$', views.Update.as_view(), name="update"),
    #  url(r'^products/$', views.viewname, name='urlname'),
    path("<pk>/", views.Detail.as_view(), name="detail"),
    path("checkout/", views.checkout, name='checkout'),
]
