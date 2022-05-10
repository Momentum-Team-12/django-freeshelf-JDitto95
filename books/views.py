from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import books
from books.forms import BookForm
from .models import Book, Category
# Create your views here.
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "books/book_detail.html", {"book": book})
    

def books_by_category(request, slug):
    category = Category.objects.get(slug+slug)
    books = Book.objects.filter(category=category)
    return render(request, 'books/books_by_category.html', {'books': books})
    