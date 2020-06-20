from rest_framework import serializers
from .models import Beer

class BeerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Beer
    # fields = ['brand', 'alcohol']
    fields = '__all__'