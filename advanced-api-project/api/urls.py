from django.urls import path
from .views import BookListView, BookDetailView
from .views import BookDeleteView
from .views import BookUpdateView
from .views import BookCreateView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
urlpatterns = [
    path('book/add/', BookCreateView.as_view(), name='book_add'),
]
urlpatterns = [
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
]
urlpatterns = [
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]