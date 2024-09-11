from django import forms

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)

class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(label='Search', max_length=100, required=False)
    chart_type = forms.ChoiceField(label='Chart Choice', choices=CHART_CHOICES, required=False)

