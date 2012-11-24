from django.forms import ModelForm, PasswordInput
from core.models import LibraryAccount


class LibraryAccountForm(ModelForm):
    class Meta:
        model = LibraryAccount
        fields = ('card_number', 'pin', 'email')
        widgets = {
            'pin' : PasswordInput(),
        }

    def clean(self):
        cleaned_data = super(LibraryAccountForm, self).clean()

        stripped_number = cleaned_data.get('card_number', '').replace(" ", "")    
        cleaned_data['card_number'] = stripped_number

        return cleaned_data
