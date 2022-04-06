from django import forms

class RegisterForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.EmailField(label='Your email', max_length=100)
    your_password = forms.CharField(label='Your password', max_length=100)