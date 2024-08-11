from django.contrib import admin

# Register your models here.
# bookshelf/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Fields to filter by
    list_filter = ('publication_year', 'author')
    
    # Fields to search
    search_fields = ('title', 'author')
