from django.db import models
from django.utils import timezone

class FoodItem(models.Model):
    """Model to store food items and their calorie information"""
    name = models.CharField(max_length=200, help_text="Name of the food item")
    calories = models.PositiveIntegerField(help_text="Number of calories")
    date_added = models.DateField(default=timezone.now, help_text="Date when food was added")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added', '-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.calories} calories"
    
    def get_calories_display(self):
        """Return calories formatted with unit"""
        return f"{self.calories} kcal"