from django.urls import path
from drinks.api.viewset import (
                                DrinksListAPIView,
                                DrinksDetailAPIView
                                )
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('drinks-list', DrinksListAPIView.as_view(), name='drinks_list'),
    # path('api/v1/<int:pk>', DrinksDetailAPIView.as_view(), name='drink_detail'),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]