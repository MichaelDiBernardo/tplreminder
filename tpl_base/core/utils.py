import datetime

from django.utils.timezone import utc

def sane_now():
    return datetime.datetime.utcnow().replace(tzinfo=utc)
