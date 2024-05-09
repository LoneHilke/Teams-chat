from django.urls import path
from . import views
app_name = "teams"

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('index/details/<int:id>', views.details, name='details'),
    path('fun/', views.fun, name='fun'),
    path('index2/jq/<int:id>', views.jq, name='jq'),
    path('index3/lh/<int:id>', views.lh, name='lh'),
    path('add_link/', views.add_link, name='add_link'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
    path('lmh/', views.lmh, name='lmh'),
]