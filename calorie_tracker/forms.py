from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    """Form for adding new food items"""
    
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Enter food name (e.g., Apple, Pizza)'
            }),
            'calories': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Enter calories',
                'min': 0
            })
        }
    
    def clean_calories(self):
        """Validate that calories is a positive number"""
        calories = self.cleaned_data.get('calories')
        if calories is None or calories < 0:
            raise forms.ValidationError('Calories must be a positive number')
        return calories
    
    def clean_name(self):
        """Validate that name is not empty"""
        name = self.cleaned_data.get('name')
        if not name or name.strip() == '':
            raise forms.ValidationError('Food name cannot be empty')
        return name.strip()