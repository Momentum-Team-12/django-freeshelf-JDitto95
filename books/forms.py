from django import forms
from .models import Book, Favorite 


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
    
        ]
        
        
class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
            
        ]