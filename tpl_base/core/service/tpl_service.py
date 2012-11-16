from lib.tplparse import *

class TPLService(object):
    def __init__(self):
        self._fetcher = TplFetcher()
        self._parser = TplParser()

    def fetch_records_for_account(self, account):
        try:
            result = self._fetcher.fetch_for_user(account.card_number, account.pin)
            records = self._parser.parse_string(result)
        except ParseError:
            # This is only thrown on no-loans. TODO: Fix this.
            records = []
        return records
