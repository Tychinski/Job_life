from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main_index'),
    path('insert/', data_page, name='data_page'),
]
