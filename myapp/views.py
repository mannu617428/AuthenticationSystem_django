from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login


from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # Use CustomUserCreationForm here
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class MyLoginView(LoginView):
    template_name = 'registration/login.html'


@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return HttpResponseForbidden('You are not authorized to view this page')
    # Add logic for admin dashboard
    return render(request, 'admin_dashboard.html')

@login_required
def regular_user_dashboard(request):
    if request.user.role != 'regular_user':
        return HttpResponseForbidden('You are not authorized to view this page')
    # Add logic for regular user dashboard
    return render(request, 'regular_user_dashboard.html')

# function based
# myapp/views.py

from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to the user dashboard URL upon successful login
            return redirect('regular_user_dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

