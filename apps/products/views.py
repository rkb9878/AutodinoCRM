from django.shortcuts import render
from .models import *
from rest_framework.generics import ListAPIView
from .serializer import CategorySerializers
# Create your views here.

def index(request):
    category = Category.objects.all()
    return render(request, 'index.html',{'category':category})

class CategoryList(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()