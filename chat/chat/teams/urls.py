from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('index/details/<int:id>', views.details, name='details'),
    path('fun/', views.fun, name='fun'),
    path('jq/', views.jq, name='jq'),
    path('lh/', views.lh, name='lh'),
    path('add_link/', views.add_link, name='add_link'),
]