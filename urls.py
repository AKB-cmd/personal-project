
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodItemViewSet, CalorieLogViewSet

router = DefaultRouter()
router.register(r'food-items', FoodItemViewSet)
router.register(r'calorie-logs', CalorieLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
