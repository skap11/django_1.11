from django import forms
from .models import RestaurantLocation


class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    category = forms.CharField(required=False)
    location = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError('Not a valid name')
        return name

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if category == 'lol':
            raise forms.ValidationError('Not a valid category')
        return category


class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category'
        ]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError('Not a valid name')
        return name

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if category == 'lol':
            raise forms.ValidationError('Not a valid category')
        return category