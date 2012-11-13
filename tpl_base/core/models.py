from django.db import models


class LibraryAccount(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255)
    card_number = models.CharField(max_length=30)
    pin = models.CharField(max_length=20)
    last_check = models.DateTimeField()
