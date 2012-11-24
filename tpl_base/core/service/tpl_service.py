import logging
logger = logging.getLogger(__name__)

from lib.tplparse import *

class TPLService(object):
    def __init__(self):
        self._fetcher = TplFetcher()
        self._parser = TplParser()

    def fetch_records_for_account(self, account):
        try:
            result = self._fetcher.fetch_for_user(account.card_number, account.get_pin())
            records = self._parser.parse_string(result)
            return records
        except ParseError:
            logger.info("Parse failed / no records for %s" %
                    account.card_number)
        except LoginError:
            logger.warning("Login failed while fetching records for %s" %
                    account.card_number)
        except Exception, e:
            logger.error("Fetch exception: %s" % e)

        return []

    def test_login(self, account):
        try:
            # We use the raw pin here b/c hasn't been saved yet. 
            # TODO: This is stupid. 
            self._fetcher.fetch_for_user(account.card_number, account.pin)
        except LoginError:
            return False
        except Exception, e:
            logger.error("Login test exception: %s" % e)

        return True
