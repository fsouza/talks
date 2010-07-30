#coding:utf-8
import unittest
from datetime import date
from nose.tools import assert_equals

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.d = date(year = 2010, month = 7, day = 30)

    def test_dateformat_filter(self):
        "dateformat filter should receive a data object and returns a formated string"
        from talks_application.filters import dateformat
        assert_equals(dateformat(self.d, '%d/%m/%Y'), '30/07/2010')

    def test_dateformat_filter_default_format(self):
        "dateformat filter should return %m/%d/%Y format when it is omitted"
        from talks_application.filters import dateformat
        assert_equals(dateformat(self.d), '07/30/2010')

    def tearDown(self):
        pass
