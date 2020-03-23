from allauth.account.forms import (SignupForm, LoginForm, ResetPasswordForm,
                                   ResetPasswordKeyForm)
from django import forms
from django.contrib.auth.models import User


# Override django allauth LoginForm
class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs['class'] = 'form2__input'

        self.fields['password'].widget = forms.PasswordInput(attrs=
                                                  {
                                                   'class': 'form2__input',
                                                   'type': "password",
                                                   'placeholder': "Password",
                                                   'id': "pass"
                                                  })


# Override django allauth SignForm
class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username')
    email = forms.EmailField(max_length=30, label='Email Address')
    password1 = forms.CharField(max_length=30, label='Password')
    password2 = forms.CharField(max_length=30, label='Confirm Password')

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
                                                   'class': 'form2__input',
                                                   'type': "text",
                                                   'placeholder': "Username",
                                                   'id': "uname"
                                                })
        self.fields['email'].widget.attrs.update({
                                                    'class': 'form2__input',
                                                    'type': "email",
                                                    'placeholder': "Email address",
                                                    'id': "email"
                                                })
        self.fields['password1'].widget.attrs.update({
                                                   'class': 'form2__input',
                                                   'type': "password",
                                                   'placeholder': "Password",
                                                   'id': "pass"
                                                   })
        self.fields['password2'].widget.attrs.update({
                                                   'class': 'form2__input',
                                                   'type': "password",
                                                   'placeholder': "Re-enter password",
                                                   'id': "pass2"
                                                   })

        def signup(self, request, user):
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.password1 = self.cleaned_data['password1']
            user.password2 = self.cleaned_data['password2']
            user.save()
            return user


# Override django allauth ResetPasswordForm
class CustomResetPasswordForm(ResetPasswordForm):
    email = forms.EmailField(max_length=50, label='Email Address')

    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form2__input'


# Override django allauth ResetPasswordKeyForm
class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
    password1 = forms.CharField(max_length=30, label='Password',
                                widget=forms.PasswordInput(attrs=
                                {
                                    'type': 'password'
                                }))
    password2 = forms.CharField(max_length=30, label='Confirm Password',
                                widget=forms.PasswordInput(attrs=
                                {
                                    'type': 'password'
                                }))

    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordKeyForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
                                            'class': 'form2__input',
                                            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
                                            'class': 'form2__input',
                                            'type': 'password',
                                            'placeholder': 'Re-enter password'
        })
