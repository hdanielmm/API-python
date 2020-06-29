from django.shortcuts import render
from rest_framework import viewsets
from .api.serializers import BeerSerializer
from .models import Beer

# Create your views here.
class BeerViewSet(viewsets.ModelViewSet):
  queryset = Beer.objects.all().order_by('brand')
  serializer_class = BeerSerializer