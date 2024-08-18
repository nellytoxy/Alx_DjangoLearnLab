# Open the Django shell
python manage.py shell

# Create a Book instance
from bookshelf.models import Book

# Create a book with title “1984”, author “George Orwell”, and publication year 1949
book = Book(title="1984", author="George Orwell", published_date=1949)
book.save()

# Confirm creation
print(book)


### 3. Retrieve the `Book` Instance
**Command:**
```python
# Retrieve the book you just created
book = Book.objects.get(title="1984")
print(book.title)
print(book.author)
print(book.published_date)


### 4. Update the `Book` Instance
**Command:**
```python
# Update the title of the book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
print(book.title)


### 5. Delete the `Book` Instance
**Command:**
```python
# Delete the book you created
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)

