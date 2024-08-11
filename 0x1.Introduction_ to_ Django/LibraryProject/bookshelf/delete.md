### 5. Delete the `Book` Instance
**Command:**
```python
# Delete the book you created
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)
