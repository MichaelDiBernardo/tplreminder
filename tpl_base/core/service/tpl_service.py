from lib.tplparse import *

class TPLService(object):
    def __init__(self):
        self._fetcher = TplFetcher()
        self._parser = TplParser()

    def fetch_records_for_account(self, account):
        try:
            result = self._fetcher.fetch_for_user(account.card_number, account.pin)
            records = self._parser.parse_string(result)
            return records
        except ParseError:
            print "No records for %s" % account.card_number
        except LoginError:
            # For now, just log it.
            print "Couldn't log in %s" % account.card_number
        except Exception, e:
            # log e
            print e

        return []

    def test_login(self, account):
        try:
            self._fetcher.fetch_for_user(account.card_number, account.pin)
        except LoginError:
            return False
        except Exception:
            pass

        return True
