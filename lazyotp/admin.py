# coding: utf-8
from django.contrib import admin

from lazyotp.forms import TOTPAuthenticationForm


class TOTPAdminSite(admin.AdminSite):
    login_form = TOTPAuthenticationForm
    login_template = "login_totp.html"
