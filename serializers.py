from rest_framework import serializers
from .models import FoodItem, CalorieLog

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'  
class CalorieLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieLog
        fields = '__all__'  
