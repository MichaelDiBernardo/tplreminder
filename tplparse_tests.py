import datetime
import unittest

from tplparse import TplParser, LoanRecord, ParseError


class TplParseTest(unittest.TestCase):
    def testFromFile(self):
        with open("source.html") as source_file:
            records = TplParser().parse_string(source_file.read())

            self.assertEquals(5, len(records))

            first = records[0]
            self.assertEquals("Uncatalogued book", first.title)
            self.assertEquals("", first.link)
            self.assertEquals(2, first.times_renewed)
            self.assertEquals(datetime.date(2012, 11, 7), first.due_date)

            second = records[1]
            self.assertEquals("Triathlons for women", second.title)
            self.assertEquals("http://www.torontopubliclibrary.ca/detail.jsp?R=2631037", second.link)
            self.assertEquals(2, second.times_renewed)
            self.assertEquals(datetime.date(2012, 11, 7), second.due_date)

            last = records[-1]
            self.assertEquals("Thrive fitness : mental and physical strength for life", last.title)
            self.assertEquals("http://www.torontopubliclibrary.ca/detail.jsp?R=2486868", last.link)
            self.assertEquals(0, last.times_renewed)
            self.assertEquals(datetime.date(2012, 11, 12), last.due_date)

    def testFailedLogin(self):
        with open("failed-login.html") as source_file:
            try:
                TplParser().parse_string(source_file.read())
                self.fail()
            except ParseError:
                pass

    def testLoanIsFine(self):
        record = LoanRecord(
            title="Blah",
            link="http://foo.com",
            times_renewed=0,
            due_date=datetime.date.today() + datetime.timedelta(days=4)
        )

        self.assertFalse(record.is_coming_due())
        self.assertFalse(record.is_overdue())

    def testLoanIsComingDue(self):
        record = LoanRecord(
            title="Blah",
            link="http://foo.com",
            times_renewed=0,
            due_date=datetime.date.today() + datetime.timedelta(days=3)
        )

        self.assertTrue(record.is_coming_due())
        self.assertFalse(record.is_overdue())

    def testLoanIsOverdue(self):
        record = LoanRecord(
            title="Blah",
            link="http://foo.com",
            times_renewed=0,
            due_date=datetime.date.today() - datetime.timedelta(days=1)
        )

        self.assertTrue(record.is_coming_due())
        self.assertTrue(record.is_overdue())

    def testCanStillBeRenewed(self):
        record = LoanRecord(
            title="Blah",
            link="http://foo.com",
            times_renewed=1,
            due_date=datetime.date.today()
        )

        self.assertTrue(record.can_be_renewed())

    def testCannotBeRenewed(self):
        record = LoanRecord(
            title="Blah",
            link="http://foo.com",
            times_renewed=3,
            due_date=datetime.date.today()
        )

        self.assertFalse(record.can_be_renewed())
