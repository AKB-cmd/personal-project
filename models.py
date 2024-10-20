from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    grams = models.FloatField(default=0.0)
    calories = models.PositiveIntegerField(default=0)
    protein = models.FloatField(default=0.0)
    fat = models.FloatField(default=0.0)
    carbohydrates = models.FloatField(default=0.0)
      

    def __str__(self):
        return self.name

class CalorieLog(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    grams = models.FloatField(default=0)  
    date = models.DateField(auto_now_add=True)
   
    def __str__(self):
        return f"{self.food_item.name} - {self.quantity}g"
