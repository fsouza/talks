import unittest
import mocker
from nose.tools import assert_equals

class TestContextProcessors(unittest.TestCase):

    def setUp(self):
        self.mocker = mocker.Mocker()

    def test_create_login_and_logout_url_injector(self):
        "Should exists a context processor to inject the Google App Engine login and logout URLs in the context"
        from google.appengine.api.users import create_login_url, create_logout_url
        from talks_application.context_processors import inject_login_url
        assert_equals(inject_login_url(), dict(create_login_url=create_login_url, create_logout_url=create_logout_url))

    def test_inject_logged_user(self):
        "Should inject the current user in the template context when there is a logged in user"
        from google.appengine.api.users import User
        user = self.mocker.mock(User)
        google_user = self.mocker.replace('google.appengine.api.users.User')
        google_user()
        self.mocker.result(user)
        self.mocker.replay()

        from talks_application.context_processors import inject_user
        assert_equals(inject_user(), dict(user=user))
        self.mocker.verify()

    def test_inject_none_when_not_logged_user(self):
        "Should inject None on user variable in the template context when there is not a logged in user"
        from google.appengine.api.users import UserNotFoundError
        google_user = self.mocker.replace('google.appengine.api.users.User')
        google_user()
        self.mocker.throw(UserNotFoundError)
        self.mocker.replay()

        from talks_application.context_processors import inject_user
        assert_equals(inject_user(), dict(user=None))
        self.mocker.verify()

    def tearDown(self):
        self.mocker.restore()

