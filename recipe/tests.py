from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Recipe

class MainViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Dessert')
        self.recipe = Recipe.objects.create(
            title='Chocolate Cake',
            description='A delicious chocolate cake',
            instructions='Mix ingredients and bake',
            ingredients='Chocolate, Flour, Sugar, Eggs',
            category=self.category
        )

    def test_main_view_status_code(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_main_view_uses_correct_template(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'recipe/main.html')

    def test_main_view_displays_recipes(self):
        response = self.client.get(reverse('main'))
        self.assertContains(response, self.recipe.title)
        self.assertContains(response, self.recipe.description)

class CategoryDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_category_detail_view_status_code(self):
        response = self.client.get(reverse('category_detail'))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view_uses_correct_template(self):
        response = self.client.get(reverse('category_detail'))
        self.assertTemplateUsed(response, 'recipe/category_detail.html')


# Create your tests here.
