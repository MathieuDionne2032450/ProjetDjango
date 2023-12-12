from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms as dforms
from django.core.mail import send_mail

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

    def save(self, commit=True):
        user = super(AddUserForm, self).save(commit=False)
        user.save()
        self.SendEmail()
        return user
    
    def SendEmail(self):
        mail = self.cleaned_data['email']
        send_mail(
            "Creation d'un compte",
            "Merci de vous d'avoir cree un compte sur ApiFruit",
            "dionne.mathieu@outlook.com",
            [mail],
            fail_silently=False,
        )

class EditUserForm(UserChangeForm):
    email = dforms.EmailField(label="Courriel", widget=dforms.EmailInput(attrs={'class': 'form-control'}))
    first_name = dforms.CharField(label="Prénom", max_length=100, widget=dforms.TextInput(attrs={'class': 'form-control'}))
    last_name = dforms.CharField(label="Nom de famille", max_length=100, widget=dforms.TextInput(attrs={'class': 'form-control'}))
    username = dforms.CharField(label="Nom d'utilisateur", max_length=100, widget=dforms.TextInput(attrs={'class': 'form-control'}))
    last_login = dforms.CharField(max_length=100, widget=dforms.HiddenInput(attrs={'class': 'form-control'}))
    is_superuser = dforms.CharField(max_length=100, widget=dforms.HiddenInput(attrs={'class': 'form-check'}))
    is_staff = dforms.CharField(max_length=100, widget=dforms.HiddenInput(attrs={'class': 'form-check'}))
    is_active = dforms.CharField(max_length=100, widget=dforms.HiddenInput(attrs={'class': 'form-check'}))
    date_joined = dforms.CharField(max_length=100, widget=dforms.HiddenInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        #dforms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['password'].widget = dforms.HiddenInput()

class ChangeUserPasswordForm(PasswordChangeForm):
    old_password = dforms.CharField(label="Mot de passe actuel", widget=dforms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = dforms.CharField(label="Nouveau mot de passe", max_length=100, widget=dforms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = dforms.CharField(label="Confirmation du mot de passe", max_length=100, widget=dforms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')




    
