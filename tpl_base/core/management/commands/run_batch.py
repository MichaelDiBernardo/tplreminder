import datetime
import logging

from django.conf import settings
from django.core import management
from django.core.management.base import NoArgsCommand

logger = logging.getLogger(__name__)

class Command(NoArgsCommand):
    help = 'Fetches loan status and sends emails for all accounts that haven\'t been checked in 24h.'

    def handle_noargs(self, **options):
        account_service = settings.CONTEXT.AccountService
        tpl_service = settings.CONTEXT.TPLService
        mail_service = settings.CONTEXT.MailService

        accounts = account_service.get_outstanding_accounts()
        logger.info("Checking {0} accounts.".format(len(accounts)))
        for account in accounts:
            records = tpl_service.fetch_records_for_account(account)
            mail_service.send_reminder_email(account, records)
            account.mark_as_checked()
