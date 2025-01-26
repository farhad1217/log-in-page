from django import forms
from .models import Registration

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Enter Your Password")
    class Meta:
        model = Registration
        fields = "__all__"
        labels = {
            "first_name": "Enter Your First Name",
            "last_name": "Enter Your Last Name",
            "email": "Enter Your Email",
            "password": "Enter Your Password"
        }
        widget = {
            "password": "PasswordInput"
        }
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Re Enter Your Password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "password dont match")
        
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput, label="Enter Your Email", error_messages={
        "required": "Email Field cannot be empty"
    })
    password = forms.CharField(widget=forms.PasswordInput, label="Enter Your Password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")
        try:
            user = Registration.objects.get(email=email)
        except Registration.DoesNotExist:
            self.add_error("email", "Email does not exist")
            return cleaned_data

        if user.password != password:
            self.add_error("password", "Password is incorrect")
            return cleaned_data