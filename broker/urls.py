from django.urls import path
from . import views
from .views import PropertyListView, PropertyDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
   # path('browse/', views.browse, name='browse'),
    path('browse/', PropertyListView.as_view(), name='browse'),
    path('details/<int:pk>', PropertyDetailView.as_view(), name='details'),
    path('fun/', views.fun, name='fun'),
]