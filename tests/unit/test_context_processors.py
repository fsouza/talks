import unittest
from nose.tools import assert_equals

class TestContextProcessors(unittest.TestCase):

    def test_create_login_and_logout_url_injector(self):
        "Should exists a context processor to inject the Google App Engine login and logout URLs in the context"
        from google.appengine.api.users import create_login_url, create_logout_url
        from talks_application.context_processors import inject_login_url
        assert_equals(inject_login_url(), dict(create_login_url=create_login_url, create_logout_url=create_logout_url))

