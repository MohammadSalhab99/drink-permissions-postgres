from rest_framework import generics
from .serializers import DrinkSerializer
from drinks.models import Drink


class DrinksListAPIView(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class DrinksDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
