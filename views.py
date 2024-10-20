from rest_framework import viewsets
from .models import FoodItem, CalorieLog
from .serializers import FoodItemSerializer, CalorieLogSerializer

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class CalorieLogViewSet(viewsets.ModelViewSet):
    queryset = CalorieLog.objects.all()
    serializer_class = CalorieLogSerializer
