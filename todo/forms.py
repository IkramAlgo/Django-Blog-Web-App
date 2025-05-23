from django import forms
from blog.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']  # Adjust according to your model
