from django import forms
from .models import User  # Import your User model
import re

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12)
    
    class Meta:
        model = User  # Use the User model defined in models.py
        fields = ['username', 'email', 'password']  # Fields to include in the form
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match("^[a-zA-Z0-9_]+$", username):  # Regex to check for special characters
            raise forms.ValidationError("Username must not contain special characters.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) > 12:
            raise forms.ValidationError("Password must be a maximum of 12 characters.")
        return password

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)  # Field for email input
    password = forms.CharField(widget=forms.PasswordInput, required=True)  # Password field with hidden input
    #remember_me = forms.BooleanField(required=False)  # Optional checkbox for "Remember Me"
