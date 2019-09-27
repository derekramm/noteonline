from django import forms
from django.forms import widgets

from note.models import Author


class LoginForm(forms.Form):
    username = forms.CharField(label='账户', required=True)
    password = forms.PasswordInput()


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        error_messages = {
            'username': {'required': '账号不能为空', },
            'password': {'required': '密码不能为空', },
            'email': {'required': '邮箱不能为空', },
        }
        widgets = {
            'password': widgets.PasswordInput()
        }
