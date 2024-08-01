from allauth.account.forms import LoginForm
from django import forms


class loginBisForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].label = ("Nom d'utilisateur")
        self.fields['password'].label = ("Mot de Passe")

        self.fields['login'].widget.attrs['placeholder'] = ("Nom d'utilisateur")
        self.fields['password'].widget.attrs['placeholder'] = ("Mot de Passe")

    def login(self, *args, **kwargs):
        
        return super(loginBisForm, self).login(*args, **kwargs)
    