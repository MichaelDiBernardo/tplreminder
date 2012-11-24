from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from django.conf import settings
from django.db import models
from core import utils


class LibraryAccount(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255)
    card_number = models.CharField(max_length=30, db_index=True)
    pin = models.CharField(max_length=256)
    last_check = models.DateTimeField()

    def mark_as_checked(self):
        """
        Tells this account to remember that it was checked against the TPL site
        as of this instant.
        """
        self.last_check = utils.sane_now()
        self.save()

    def encrypt_pin(self):
        e = AES.new(settings.SECRET_KEY[:32])
        self.pin = b64encode(e.encrypt(self.pin.ljust(32)))

    def get_pin(self):
        e = AES.new(settings.SECRET_KEY[:32])
        pin = e.decrypt(b64decode(self.pin)).strip()
        return pin
