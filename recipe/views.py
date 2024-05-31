from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .models import Recipe

def main(request):
    recipes = Recipe.objects.all()  # Fetch all recipes
    return render(request, 'recipe/main.html', {'recipes': recipes})

def category_detail(request):
    return render(request, 'recipe/category_detail.html')