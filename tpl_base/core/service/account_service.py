import datetime

from core.models import LibraryAccount
from core import utils


class AccountService(object):

    def register_new(self, account):
        # This will save it also.
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
