from django.shortcuts import render
from rest_framework import generics

from . import models
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
