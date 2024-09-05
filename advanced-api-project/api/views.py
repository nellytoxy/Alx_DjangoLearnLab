from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .seriealizers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

class BookListView(generics.ListCreateAPIView):
    """
    API view to list all books or create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_update(self, serializer):
        # Custom logic before updating a book instance
        serializer.save()

    def perform_destroy(self, instance):
        # Custom logic before deleting a book instance
        instance.delete()
        
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Book
from .forms import BookForm

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')  # Redirect to a list of books after 
    
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')  
    
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')  

        
from rest_framework import generics
from .models import Book
from .seriealizers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListCreateView(generics.ListCreateAPIView):
    """
    API view to list all books or create a new book.
    - **GET /books/**: Retrieve a list of all books.
    - **POST /books/**: Create a new book instance. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a book instance.
    - **GET /books/<int:pk>/**: Retrieve a single book by ID.
    - **PUT /books/<int:pk>/**: Update an existing book instance. Requires authentication.
    - **DELETE /books/<int:pk>/**: Delete a book instance. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



# Create your views here.
