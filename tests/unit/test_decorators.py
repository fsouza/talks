import unittest
import mocker
from contextlib import nested
from google.appengine.api import users
from nose.tools import assert_equals

class TestDecorators(unittest.TestCase):

    def setUp(self):
        self.mocker = mocker.Mocker()

    def tearDown(self):
        self.mocker.restore()

    def bad_mock(self):
        kwargs = {}

        google_user = self.mocker.replace('google.appengine.api.users.User')
        google_user()
        self.mocker.throw(users.UserNotFoundError)

        url_for_mock = self.mocker.replace('flask.url_for')
        url_for_mock('say_hi', _external = True, **kwargs)
        self.mocker.result('anything')

        login_url_mock = self.mocker.replace('google.appengine.api.users.create_login_url')
        login_url_mock('anything')
        self.mocker.result('/')

        redirect_mock = self.mocker.replace('flask.redirect')
        redirect_mock('/')
        self.mocker.result('Bye!')

        self.mocker.replay()

    def good_mock(self):
        google_user = self.mocker.replace('google.appengine.api.users.User')
        google_user()
        self.mocker.result('Anything else')

        self.mocker.replay()

    def test_changes_function(self):
        'When there is no user logged, should not call the original function'

        self.bad_mock()

        from talks_application.decorators import login_required
        @login_required
        def say_hi():
            return 'Hi!'

        assert_equals(say_hi(), 'Bye!');

    def test_no_changes_function(self):
        "When there is a user logged, should call the original function"
        self.good_mock()

        from talks_application.decorators import login_required
        @login_required
        def say_hi():
            return 'Hi!'

        assert_equals(say_hi(), 'Hi!')

    def test_ignores_function(self):
        "When a function is not decorated, should not touch it"
        def say_hi():
            return 'Hi!'

        assert_equals(say_hi(), 'Hi!')
