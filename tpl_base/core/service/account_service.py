import datetime

from core.models import LibraryAccount
from core import utils


class AccountService(object):
    def get(self, card_number):
        try:
            return LibraryAccount.objects.filter(card_number=card_number).get()
        except LibraryAccount.DoesNotExist:
            return None

    def register_new(self, account):
        # See if they've registered before. If so, overwrite.
        old_account = self.get(account.card_number)
        if old_account:
            old_account.delete()

        # Marking as checked also saves.
        account.mark_as_checked()
        return account

    def get_outstanding_accounts(self):
        """
        Fetch all those accounts that we need to check against the TPL website.
        In this case, that means any account we haven't checked in 24h.
        """
        yesterday = utils.sane_now() - datetime.timedelta(days=1)
        accounts = LibraryAccount.objects.filter(last_check__lt=yesterday)

        return accounts
    
    def unsubscribe(self, account):
        # Well, that was easy.
        account.delete()
