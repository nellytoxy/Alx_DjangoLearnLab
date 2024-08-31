# Open the Django shell
python manage.py shell

# Create a Book instance
from bookshelf.models import Book

# Create a book with title “1984”, author “George Orwell”, and publication year 1949
Book.objects.create
book = Book(title="1984", author="George Orwell", published_date=1949)
book.save()

# Confirm creation
print(book)