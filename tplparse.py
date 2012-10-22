import datetime
import re
import requests

from bs4 import BeautifulSoup


class LoanRecord(object):
    def __init__(self, title, link, times_renewed, due_date):
        self.title = title
        self.link = link
        self.times_renewed = times_renewed
        self.due_date = due_date

    def days_until_due(self):
        today = datetime.date.today()
        return (self.due_date - today).days

    def is_loan_coming_due(self):
        return self.days_until_due() <= 3

    def is_loan_overdue(self):
        return self.days_until_due() < 0

    def renewals_left(self):
        return 3 - self.times_renewed

    def can_be_renewed(self):
        return self.renewals_left() > 0


class TplParser(object):
    def parse_string(self, html_string):
        soup = BeautifulSoup(html_string)
        renewal_table = soup.find(id="renewcharge")
        hold_records = renewal_table.find_all('tr')

        return [self._parse_record(r) for r in hold_records]

    def _parse_record(self, record):
        cells = record.find_all('td')

        title_cell = cells[1]
        try:
            book_link_tag = title_cell.find('a')
            book_href = book_link_tag.attrs['href']
            book_name = book_link_tag.text.strip()
        except AttributeError:
            book_name = "Uncatalogued book"
            book_href = ""

        times_renewed_cell = cells[2]

        try:
            times_renewed = int(times_renewed_cell.find('strong').text)
        except ValueError:
            times_renewed = 0

        due_date_cell = cells[3]
        due_date_match = re.search(
            r'(\d+/\d+/\d+)', due_date_cell.text).group(1)
        due_date = datetime.datetime.strptime(
            due_date_match, "%d/%m/%Y").date()

        return LoanRecord(
            title=book_name,
            link=book_href,
            times_renewed=times_renewed,
            due_date=due_date
        )


class TplFetcher(object):

    SIGNIN_URL = 'https://www.torontopubliclibrary.ca:443/signin?target=youraccount'

    def fetch_for_user(self, user_id, pin):
        with requests.session() as browser:
            data = {
                'userId': user_id,
                'password': pin
            }

            response = browser.post(self.SIGNIN_URL, data=data)
            return response.text
