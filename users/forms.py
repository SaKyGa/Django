from django import forms


class RegisterForm(forms.Form):
    avatar = forms.ImageField()
    age = forms.IntegerField()
    username = forms.CharField(max_length=150)
    password = forms.CharField()
    password_confirm = forms.CharField()



class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)