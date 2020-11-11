from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Login",
                'maxlength': "20",
                'minlength': "5"
            }),
            'password': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Password",
                'minlength': "5",
                'type': "password"
            })
        }

