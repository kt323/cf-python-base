from django.test import TestCase
from .models import Recipes

class RecipesModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Recipes.objects.create(
            name='Salad',
            cooking_time=5,  # Ensure this matches your model's field type
            ingredients='veggies, tomato, dressing sauce',
            description='Add everything together and mix it'
        )

    def test_recipes_name(self):
        recipes = Recipes.objects.get(id=1)
        field_label = recipes._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_recipes_name_max_length(self):
        recipes = Recipes.objects.get(id=1)
        max_length = recipes._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)

