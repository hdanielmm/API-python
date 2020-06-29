from rest_framework.generics import ListAPIView, RetrieveAPIView

from productos.models import Beer
from .serializers import BeerSerializer

class BeerListView(ListAPIView):
  queryset = Beer.objects.all()
  serializer_class = BeerSerializer

class BeerDetailView(RetrieveAPIView):
  queryset = Beer.objects.all()
  serializer_class = BeerSerializer