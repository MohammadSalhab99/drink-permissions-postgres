from rest_framework import generics
from .serializers import DrinkSerializer
from drinks.models import Drink
from .permissions import IsOwnerOrReadOnly



class DrinksListAPIView(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class DrinksDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = (IsOwnerOrReadOnly)

