from rest_framework import serializers
from drinks.models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','description','name')
        model = Drink