from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from models import Book

@login_required
@permission_required('myapp.can_view_mymodel', raise_exception=True)
def view_mymodel(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    # Your view logic here
    return render(request, 'myapp/view_mymodel.html', {'instance': instance})

@login_required
@permission_required('myapp.can_create_mymodel', raise_exception=True)
def create_mymodel(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'myapp/create_mymodel.html')

@login_required
@permission_required('myapp.can_edit_mymodel', raise_exception=True)
def edit_mymodel(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'myapp/edit_mymodel.html', {'instance': instance})

@login_required
@permission_required('myapp.can_delete_mymodel', raise_exception=True)
def delete_mymodel(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('book_list", "books')
    return render(request, 'advanced_features_and_security/delete_book.html', {'instance': instance})


# Create your views here.
