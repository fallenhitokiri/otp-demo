# coding: utf-8
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

import pyotp


class TOTPAuthenticationForm(AuthenticationForm):
    token = forms.CharField(max_length=6)

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)

        if not hasattr(user, "token"):
            raise ValidationError("User not setup for token based authentication")

        secret = user.token.secret
        token = self.cleaned_data.get("token")

        totp = pyotp.TOTP(secret)

        if not totp.verify(token):
            raise ValidationError("Invalid token")
