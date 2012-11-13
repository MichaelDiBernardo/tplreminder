from django.forms import ModelForm
from core.models import LibraryAccount


class LibraryAccountForm(ModelForm):
    class Meta:
        model = LibraryAccount
        fields = ('card_number', 'pin', 'email')
