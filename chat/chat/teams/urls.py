from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('index/details/<int:id>', views.details, name='details'),
    path('fun/', views.fun, name='fun'),
    path('jq/', views.jq, name='jq'),
    path('lh/<int:id>', views.lh, name='lh'),
]