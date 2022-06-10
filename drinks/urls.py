from django.urls import path
from drinks.api.viewset import (
                                DrinksListAPIView,
                                DrinksDetailAPIView
                                )
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/v1/drinks-list', DrinksListAPIView.as_view(), name='drinks_list'),
    path('api/v1/<int:pk>', DrinksDetailAPIView.as_view(), name='drink_detail'),
    path('api/v1/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]
# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDE4NjMwMywiaWF0IjoxNjU0MDk5OTAzLCJqdGkiOiI0MTMxNzUwYTIxMjQ0MWUyOTFmYzZlYTA5MzJjZDA5ZCIsInVzZXJfaWQiOjF9.V8VJghWRptOemP_F0ZjFk9_B-5n7imvh-goDw8TMIKo",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MTAwMjAzLCJpYXQiOjE2NTQwOTk5MDMsImp0aSI6ImJmMDNhMzdmZDQzMTQ3NWM5NDA1NTVmMjRkOTc2N2UzIiwidXNlcl9pZCI6MX0.1geRCZO5Noc6058GiOA3S8JJKtE0cGvDHAo8c3d_YB4"
# }