from django.urls import path
from .views import *

app_name='product'

urlpatterns = [
    path('', index, name="home"),
    path('category', CategoryList.as_view(), name="categoryApi")
]