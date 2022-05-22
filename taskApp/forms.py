from django.forms import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Username..."
            }
        )
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Password..."
            }
        )
    )
