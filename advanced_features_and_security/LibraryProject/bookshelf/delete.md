### 5. Delete the `Book` Instance
**Command:**
```python
# Delete the book you created
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)
