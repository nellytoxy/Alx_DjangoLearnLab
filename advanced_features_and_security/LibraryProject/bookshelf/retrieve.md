# Retrieve the book you just created
book = Book.objects.get(title="1984")
print(book.title)
print(book.author)
print(book.published_date)