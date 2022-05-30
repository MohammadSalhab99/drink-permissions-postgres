from django.urls import path
from drinks.api.viewset import (
                                DrinksListAPIView,
                                DrinksDetailAPIView
                                )

urlpatterns = [
    path('api/v1/drinks-list', DrinksListAPIView.as_view(), name='drinks_list'),
    path('api/v1/<int:pk>', DrinksDetailAPIView.as_view(), name='drink_detail'),

]