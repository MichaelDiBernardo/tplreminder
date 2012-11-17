import logging
logger = logging.getLogger(__name__)

from django.template import Context, loader
from django.core.mail import EmailMultiAlternatives


class MailService(object):
    def send_reminder_email(self, account, records):
        record_set = LoanRecordSetPresenter(records)

        if record_set.is_empty():
            return

        c = Context({ 
            "overdue": record_set.overdue, 
            "coming_due": record_set.coming_due,
        })
        text_template = loader.get_template("notification-email.txt")
        text_message = text_template.render(c)

        html_template = loader.get_template("notification-email.html")
        html_message = html_template.render(c)

        subject = "Library book reminder"

        msg = EmailMultiAlternatives(
                subject,
                text_message,
                "noreply@tplreminder.ca",
                (account.email,)
        )
        msg.attach_alternative(html_message, "text/html")

        try:
            msg.send()
        except Exception, e:
            logger.error("Mail for %s failed: '%s'" % (account.card_number, e))


# TODO: Maybe this belongs somewhere smarter? maybe as returnval for parser
# instead of a presenter.
class LoanRecordSetPresenter(object):
    def __init__(self, records):
        self.coming_due = [r for r in records if r.is_coming_due()]
        self.overdue = [r for r in records if r.is_overdue()]

    def is_empty(self):
        return not (self.coming_due or self.overdue)
