from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from .models import User_profile
from django.core.mail import EmailMessage
from django.conf import settings 

class EventRegisterForm(forms.Form):
    event_name = forms.CharField(
        min_length = 5,
        widget = forms.TextInput(attrs={'type': 'Text'}))
    info = forms.EmailField(
        widget = forms.EmailInput(attrs={'type': 'email', 'class': 'validate'}))
    when = forms.DateField(
        widget =  SelectDateWidget(empty_label=("A&ntilde;io", "Mes", "D&iacute;a"))
        )
    ends = forms.DateField(
        widget =  SelectDateWidget(empty_label=("A&ntilde;io", "Mes", "D&iacute;a"))
        )
    cover_price = forms.DecimalField(
        decimal_places = 2,
        widget = forms.NumberInput(attrs={'type': 'text'}))
    cover_image = forms.ImageField(
        required=False, 
        widget = forms.FileInput(attrs={'type': 'file', 'class': 'cyan'}))
    hashtags = forms.CharField(
        min_length = 2,
        widget = forms.TextInput(attrs={'type': 'Text'}))
    location = forms.CharField(
        min_length = 5,
        widget = forms.TextInput(attrs={'type': 'Text'}))
    def clean_event_name(self):
        event_name = self.cleaned_data['event_name']
        if Event.objects.filter(event_name=event_name):
            raise forms.ValidationError('Este nombre de evento ya esta registrado.')
        return event_name
    
class LocationRegisterForm(forms.Form):
    pass
    
class CommertialRegisterForm(forms.Form):
    user_name = forms.CharField(
        max_length=45,
        widget = forms.TextInput(attrs={'type': 'text', 'lenght': '45'}))
    description = forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={'type': 'text', 'lenght': '100'}))
    commertial_image = forms.ImageField(
        widget = forms.FileInput(attrs={'type': 'file'}))
    price_initial = forms.DecimalField(
        decimal_places = 2,
        widget = forms.NumberInput(attrs={'type': 'text'}))
    price_final = forms.DecimalField(
        decimal_places = 2,
        widget = forms.NumberInput(attrs={'type': 'text'}))
    username = forms.CharField(
        min_length = 5,
        widget = forms.TextInput(attrs={'type': 'Text'}))
    photo = forms.ImageField(
        required=False, 
        widget = forms.FileInput(attrs={'type': 'file', 'class': 'cyan'}))
    username = forms.CharField(
        min_length = 5,
        widget = forms.TextInput,
        label = 'Usuario'
        )
    first_name = forms.CharField(
        widget = forms.TextInput(attrs={'type': 'Text'}),
        label = 'Nombre'
        )
    last_name = forms.CharField(
        min_length = 35,
        widget = forms.TextInput(attrs={'type': 'Text'}),
        label = 'Apellido'
        )
    identification = forms.IntegerField(
        widget = forms.NumberInput(attrs={'type': 'text', 'lenght': '13'})
        )
    birthday = forms.DateField(
        widget =  SelectDateWidget(empty_label=("A&ntilde;io", "Mes", "D&iacute;a"))
        )
    phone_1 = forms.IntegerField(
        widget = forms.NumberInput(attrs={'type': 'tel', 'class': 'validate'})
        )
    phone_2 = forms.NumberInput(attrs={'type': 'tel', 'class': 'validate'})
    photo = forms.ImageField(
        required = False)
    
class RegisterUserForm(forms.Form):
    username = forms.CharField(
        min_length = 5,
        widget = forms.TextInput,
        label = 'Usuario'
        )
    first_name = forms.CharField(
        widget = forms.TextInput(attrs={'type': 'Text'}),
        label = 'Nombre'
        )
    last_name = forms.CharField(
        min_length = 35,
        widget = forms.TextInput(attrs={'type': 'Text'}),
        label = 'Apellido'
        )
    identification = forms.IntegerField(
        widget = forms.NumberInput(attrs={'type': 'text', 'lenght': '13'})
        )
    birthday = forms.DateField(
        widget =  SelectDateWidget(empty_label=("A&ntilde;io", "Mes", "D&iacute;a"))
        )
    phone_1 = forms.IntegerField(
        widget = forms.NumberInput(attrs={'type': 'tel', 'class': 'validate'})
        )
    phone_2 = forms.NumberInput(attrs={'type': 'tel', 'class': 'validate'})
    photo = forms.ImageField(
        required = False)

class ProfileRegisterForm(forms.Form):
    username = forms.CharField(
        min_length = 5,
        widget = forms.TextInput(attrs={'type': 'Text'}))
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={'type': 'email', 'class': 'validate'}))
    password = forms.CharField(
        min_length = 5, 
        widget = forms.PasswordInput(attrs={'type': 'password'}))
    password2 = forms.CharField(
        min_length = 5,
        widget = forms.PasswordInput(attrs={'type': 'password'}))

    def save(self, datas):
        user_model = User.objects.create_user(datas['username'], datas['email'], datas['password'])
        user_model.is_active = False
        user_model.save()
        user_profile = User_profile()
        user_profile.user = user_model
        user_profile.user_name = datas['username']
        user_profile.activation_key=datas['activation_key']
        user_profile.key_expires=datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
        user_profile.save()
        return user_model

#Sending activation email ------>>>!! Warning : Domain name is hardcoded below !!<<<------
    #The email is written in a text file (it contains templatetags which are populated by the method below)
    def sendEmail(self, datas):
        link="127.0.0.1:8000/login/activate/"+datas['activation_key']
        c = Context({'activation_link':link,'username':datas['username']})
        f = open(MEDIA_ROOT+datas['email_path'], 'r')
        t = Template(f.read())
        f.close()
        message=t.render(c)
        try:
            email = EmailMessage('objects', 'asdasdasdf aasd', to=['solovino.16.2012@gmail.com'], fail_silently=False)
            email.send()
            import pdb; pdb.set_trace()
        except BadHeaderError:
            return HttpResponse('Error al enviar email.')

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