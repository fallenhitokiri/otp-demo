# coding: utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

import pyotp

from lazyotp.models import Token


class Command(BaseCommand):
    help = "Generate a secret for user for TOTP authentication"

    def add_arguments(self, parser):
        parser.add_argument("user_id", type=int)

    def handle(self, *args, **options):
        user = User.objects.get(id=options["user_id"])
        secret = pyotp.random_base32()
        Token.objects.create(user=user, secret=secret)
        self.stdout.write(self.style.SUCCESS(f"Secret generated {secret}"))
