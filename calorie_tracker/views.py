from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum
from .models import FoodItem
from .forms import FoodItemForm

def index(request):
    """Main view to display today's food items and total calories"""
    today = timezone.now().date()
    
    # Get today's food items
    today_foods = FoodItem.objects.filter(date_added=today)
    
    # Calculate total calories for today
    total_calories = today_foods.aggregate(Sum('calories'))['calories__sum'] or 0
    
    # Form for adding new food
    form = FoodItemForm()
    
    context = {
        'foods': today_foods,
        'total_calories': total_calories,
        'form': form,
        'today': today,
    }
    
    return render(request, 'calorie_tracker/index.html', context)

def add_food(request):
    """View to add a new food item"""
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.date_added = timezone.now().date()
            food_item.save()
            messages.success(request, f'{food_item.name} added successfully!')
        else:
            messages.error(request, 'Please correct the errors below.')
    
    return redirect('index')

def delete_food(request, food_id):
    """View to delete a food item"""
    food_item = get_object_or_404(FoodItem, id=food_id)
    food_name = food_item.name
    food_item.delete()
    messages.success(request, f'{food_name} removed successfully!')
    return redirect('index')

def reset_today(request):
    """View to reset/delete all food items for today"""
    today = timezone.now().date()
    deleted_count = FoodItem.objects.filter(date_added=today).delete()[0]
    
    if deleted_count > 0:
        messages.success(request, f'Reset successful! Removed {deleted_count} food item(s).')
    else:
        messages.info(request, 'No food items to reset for today.')
    
    return redirect('index')