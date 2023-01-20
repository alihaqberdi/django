from django.shortcuts import render
from .models import Women
from rest_framework import generics
from .serializers import WomenSerilizers
# Create your views here.


class WomenApiView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerilizers


