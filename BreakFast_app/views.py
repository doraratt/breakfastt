from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
#from BreakFast_app.models import User
from .forms import SignupForm
from django.conf import settings
from django.urls import reverse

# Login logic
# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Authenticate user
#         try:
#           user = User.objects.get(email=email)
#           if user.check_password(password):
#               auth_login(request, user)  # Log in the user
#               return redirect('details')  # Redirect to a success page
#           else:
#               messages.error(request, "Invalid email or password.")
#         except User.DoesNotExist:
#           messages.error(request, "Invalid email or password.")
#     return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect(reverse('home'))  # Redirects to lp1.html
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login.html')

# Signup logic
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the user instance to the database

            user.backend = 'BreakFast_app.backends.EmailBackend'
            auth_login(request, user)  # Automatically log the user in
            
            return redirect('login')  # Redirect to a specific view after signup
    else:
        form = SignupForm()  # New instance of the form
        
    return render(request, 'signup.html', {'form': form})  # Render the form in the template

#profile logic
def profile(request):
    return render(request, 'profile.html')

#homepage after login
def home(request):
    return render(request, 'home.html')

#tracker
def tracker(request):
    if request.method == 'POST':
        fasting_hours = request.POST.get('fasting_hours')
        eating_hours = request.POST.get('eating_hours')
        fasting_days = request.POST.get('fasting_days')
        eating_days = request.POST.get('eating_days')

        # Save data to session (or process further as needed)
        if fasting_hours and eating_hours:
            request.session['fasting_hours'] = fasting_hours
            request.session['eating_hours'] = eating_hours
        if fasting_days and eating_days:
            request.session['fasting_days'] = fasting_days
            request.session['eating_days'] = eating_days

        return redirect('tracker')

    # Retrieve session data to display
    fasting_hours = request.session.get('fasting_hours')
    eating_hours = request.session.get('eating_hours')
    fasting_days = request.session.get('fasting_days')
    eating_days = request.session.get('eating_days')

    context = {
        'fasting_hours': fasting_hours,
        'eating_hours': eating_hours,
        'fasting_days': fasting_days,
        'eating_days': eating_days,
    }
    return render(request, 'tracker.html', context)


def program(request):
    return render(request, 'program.html')

def plan(request):
    return render(request, 'plan.html')

def me(request):
    return render(request, 'me.html')

def landing(request):
    return render(request, 'landing.html')

def personalinfo(request):
    return render(request, 'personalinfo.html')

def accountinfo(request):
    return render(request, 'accountinfo.html')