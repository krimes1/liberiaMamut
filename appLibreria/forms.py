from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import libro

class UserForm(UserCreationForm):
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={
        'class':'form-control', 
        'placeholder': 'Contraseña',
        'id':'loginPassword'
    }))
    
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={
        'class':'form-control', 
        'placeholder': 'Confirmar Contraseña',
        'id':'loginPassword2'
    }))

    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
        help_texts={k:"" for k in fields }
        labels={
            'username': 'Nombre de usuario', 
            'email': 'Correo electrónico',
            'password1': 'Contraseña', 
            'password2': 'Confirmar contraseña'
        }
        widgets={
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placegolder': 'Nombre de usuario'
            }), 

            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingresar correo'    
            }), 
        }
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario',
                                widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre de usuario'}))
    password = forms.CharField(label='Contraseña',
                                widget=forms.PasswordInput(attrs={'class': 'form-control ','placeholder':'Contraseña'}))

class LibroForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = ['nombre_libro', 'autor', 'fec_salida_libro', 'precio', 'desc_libro', 'portada_libro']
