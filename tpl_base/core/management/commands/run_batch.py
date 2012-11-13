import datetime

from django.core import management
from django.template import Context, Template, loader
from django.core.management.base import NoArgsCommand
from django.utils.timezone import utc

from core.models import LibraryAccount
from lib.tplparse import *


class Command(NoArgsCommand):
    help = 'Fetches loan status and sends emails for all accounts that haven\'t been checked in 24h.'

    def handle_noargs(self, **options):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        yesterday = now - datetime.timedelta(seconds=1)
        accounts = LibraryAccount.objects.filter(last_check__lt=yesterday)

        fetcher = TplFetcher()
        parser = TplParser()
        for account in accounts:
            try:
                result = fetcher.fetch_for_user(account.card_number, account.pin)
                records = parser.parse_string(result)
                c = Context({ "loans": records })
                t = loader.get_template("notification-email.txt")
                message = t.render(c)
                send_mail('Library book reminder', message, 'reminder@noreply.com', [account.email])
            except ParseError:
                # This is only thrown on no-loans.
                pass
            except Exception, e:
                # log e
                print e
            account.last_checked = datetime.datetime.utcnow().replace(tzinfo=utc)
