# coding: utf-8
from django.contrib.admin.apps import AdminConfig


class TOTPAdminConfig(AdminConfig):
    default_site = "lazyotp.admin.TOTPAdminSite"
