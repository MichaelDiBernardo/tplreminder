from django.core.mail import send_mail
from django.template import Context, Template, loader

class MailService(object):
    def send_reminder_email(self, account, records):
        c = Context({ "loans": records })
        t = loader.get_template("notification-email.txt")
        message = t.render(c)
        send_mail('Library book reminder', message, 'reminder@noreply.com', [account.email])
