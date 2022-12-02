from django import forms
from allauth.account.forms import SignupForm, LoginForm
from accounts.models import CustomUser

class SignupForm(SignupForm):

    class Meta:
        model = CustomUser
        fields = ('user_address1','user_address2','user_tel','user_hospital',)

class LoginForm(LoginForm):
    pass
        
