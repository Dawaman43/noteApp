from django import forms
from .models import Notes, Category

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['note_title', 'note', 'file', 'category']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 4}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']