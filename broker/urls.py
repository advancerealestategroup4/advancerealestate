from django.contrib import admin
from django.urls import path
from .import views
from .views import PropertyListView, PropertyDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('filter/', views.browse, name='browse'),
    path('browse/', PropertyListView.as_view(), name='browse'),
    path(r'^details/(?P<pk>[0-9]+)\\Z', PropertyDetailView.as_view(), name='details'),
    path('fun/', views.fun, name='fun'),
    path('success/', views.success, name='success'),



]
