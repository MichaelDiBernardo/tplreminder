from django.db import models
from core import utils


class LibraryAccount(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255)
    card_number = models.CharField(max_length=30)
    pin = models.CharField(max_length=20)
    last_check = models.DateTimeField()

    def mark_as_checked(self):
        """
        Tells this account to remember that it was checked against the TPL site
        as of this instant.
        """
        self.last_check = utils.sane_now()
        self.save()
