from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': 'input__field',
            }),
            'name': forms.TextInput(attrs={
                'class': 'input__field',
            }),
            'description': forms.Textarea(attrs={
                'class': 'input__field input__field--textarea',
            }),
            'price': forms.TextInput(attrs={
                'class': 'input__field',
            }),
            'image': forms.FileInput(attrs={
                'class': 'input__field',
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full py-6 px-6 rounded-xl border',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-6 px-6 rounded-xl border',
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full py-6 px-6 rounded-xl border',
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-6 px-6 rounded-xl border',
            }),
        }