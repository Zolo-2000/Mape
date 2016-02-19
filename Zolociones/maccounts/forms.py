from django import forms
from django.contrib.auth.models import User

class RegisterUserForm(forms.Form):
    username = forms.CharField(min_length=5)
    email = forms.EmailField()
    password = forms.CharField(min_length=5, widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    photo = forms.ImageField(required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Este nombre de usuario ya esta registrado.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un usuario con ese e-mail, puedes desactivar desactivar una cuenta.')
        return email

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contrase&ntilde;as no coinciden.')
        return password