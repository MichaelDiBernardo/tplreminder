import datetime

from django.test import TestCase

from core.models import LibraryAccount
from core.utils import sane_now
from core.service.account_service import AccountService


class AccountServiceTest(TestCase):
    def setUp(self):
        self._sut = AccountService()

    def test_get_outstanding(self):
        five_days_ago = sane_now() - datetime.timedelta(days=5)
        fake_acct('1', five_days_ago)
        fake_acct('2', five_days_ago)
        fake_acct('3', sane_now())

        # This guy was created long ago and last checked just now, so he
        # shouldn't show up in results.
        a = fake_acct('4', sane_now())
        a.creation_time = five_days_ago
        a.save()

        results = self._sut.get_outstanding_accounts()
        self.assertEquals(3, len(results))
        

def fake_acct(cn, lc):
    a = LibraryAccount(
        email="someemail@email.com",
        card_number=cn,
        pin="1234",
        last_check=lc
    )
    a.save()
    return a
