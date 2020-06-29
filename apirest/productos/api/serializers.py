from rest_framework import serializers
from productos.models import Beer

# class BeerSerializer(serializers.HyperlinkedModelSerializer):
class BeerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Beer
    # fields = ['brand', 'alcohol']
    fields = '__all__'