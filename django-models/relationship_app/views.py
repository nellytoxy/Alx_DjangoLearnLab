from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book # Ensure both models are imported
from .models import Library 

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    # relationship_app/views.py
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a 'home' page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a 'home' page after successful login
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'registration/login.html')

# User Logout View
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Library

def role_required(role):
    def in_roles(user):
        return user.userprofile.role == role
    return user_passes_test(in_roles)

@login_required
@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
