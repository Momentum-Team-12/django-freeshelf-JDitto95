from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import books
from books.forms import BookForm, FavoriteForm
from .models import Book, Category
# Create your views here.
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})

def book_detail(request, pk):
    form = FavoriteForm()
    book = Book.objects.get(pk=pk)
    return render(request, "books/book_detail.html", {"book": book})
    

def books_by_category(request, slug):
    category = Category.objects.get(slug+slug)
    books = Book.objects.filter(category=category)
    return render(request, 'books/books_by_category.html', {'books': books})
  
  
  
# def add_favorite(request,pk):
#     if request.method =='post':
#         book = get_object_or_404(Book,pk=pk)
#         user=request.user
#         form = FavoriteForm(data=request.POST)
#         if form.is_valid():
#             favorite = form.save(commit=False)
#             favorite.book=book
#             favorite.user=user
#             favorite.save()
#             return redirect(to='book_detail')