from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms as dforms

class AddUserForm(UserCreationForm):
    email = dforms.EmailField(label="Courriel", widget=dforms.EmailInput(attrs={'class': 'form-control'}))
    first_name = dforms.CharField(label="Prénom", max_length=100, widget=dforms.TextInput(attrs={'class': 'form-control'}))
    last_name = dforms.CharField(label="Nom de famille", max_length=100, widget=dforms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'