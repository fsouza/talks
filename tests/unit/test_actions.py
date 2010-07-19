import mocker
import unittest

class TestActions(unittest.TestCase):

    def setUp(self):
        self.mocker = mocker.Mocker()

    def _mock_render(self, template):
        mocked_render = self.mocker.replace('flask.render_template')
        mocked_render(template, mocker.KWARGS)
        self.mocker.result('Anything')

    def _mock_google_user(self):
        mocked_google_user = self.mocker.replace('google.appengine.api.users.User')
        mocked_google_user()
        self.mocker.result('nothing')

    def _mock_talk_form(self, result):
        mocked_talk_form = self.mocker.replace('talks_application.forms.TalkForm')
        mocked_talk_form()
        self.mocker.result(result)

    def _mock_redirect(self, destination):
        mocked_redirect = self.mocker.replace('flask.redirect')
        mocked_redirect(destination)
        self.mocker.result('Redirected...')

    def _mock_url_for(self, result_url):
        mocked_url_for = self.mocker.replace('flask.url_for')
        mocked_url_for(mocker.ANY)
        self.mocker.result(result_url)

    def _mock_complete_form(self):
        form = self.mocker.mock()
        form.title = self.mocker.mock()
        form.title.data
        self.mocker.result('The title')

        import datetime
        date = datetime.datetime.strptime('07/15/2010', '%m/%d/%Y')

        form.date = self.mocker.mock()
        form.date.data
        self.mocker.result(datetime.date(year = date.year, month = date.month, day = date.day))

        form.description = self.mocker.mock()
        form.description.data
        self.mocker.result('The description')

        form.validate_on_submit()
        self.mocker.result(True)

        return form

    def _mock_talk_with_put(self):
        talk = self.mocker.mock()
        talk.put()
        self.mocker.result(True)

        mocked_talk = self.mocker.replace('talks_application.models.Talk')
        mocked_talk(mocker.KWARGS)
        self.mocker.result(talk)

    def test_index_action(self):
        "Index action should list all talks ordered by date desc and render the /talks/index.html template"
        mocked_talk = self.mocker.replace('talks_application.models.Talk')
        mocked_talk.all().order('-date')
        self._mock_render('/talks/index.html')
        self.mocker.replay()

        from talks_application.actions import index
        index()
        self.mocker.verify()

    def test_redirect_to_logout_action(self):
        "redirect_to_logout action should redirect to a url returned by users.create_logout_url (Google API)"
        mocked_create_login = self.mocker.replace('google.appengine.api.users.create_logout_url')
        mocked_create_login('/')
        self.mocker.result('http://www.anything.com/logout')
        self._mock_redirect('http://www.anything.com/logout')
        self.mocker.replay()

        from talks_application.actions import redirect_to_logout
        redirect_to_logout()
        self.mocker.verify()

    def test_new_talk_action(self):
        "new_talk action should create a new instance of TalkForm and render /talks/new.html template"
        self._mock_talk_form(None)
        self._mock_render('/talks/new.html')
        self._mock_google_user()

        self.mocker.replay()

        from talks_application.actions import new_talk
        new_talk()
        self.mocker.verify()

    def test_create_talk_action_invalid_data(self):
        "create_talk action should render again the /talks/new.html when validate returns false"
        form = self.mocker.mock()
        form.validate_on_submit()
        self.mocker.result(False)
        self._mock_talk_form(form)
        self._mock_render('/talks/new.html')
        self._mock_google_user()
        self.mocker.replay()

        from talks_application.actions import create_talk
        create_talk()
        self.mocker.verify()

    def test_create_talk_action_valid_data(self):
        "create_talk action should create an instance of TalkForm, validate it, put a talk on the database," \
        "stores a message in flash and redirect to index."

        form = self._mock_complete_form()
        self._mock_talk_form(form)

        mocked_google_user = self.mocker.replace('google.appengine.api.users.User')
        mocked_google_user()
        self.mocker.count(1, 2)

        self._mock_talk_with_put()

        mocked_flash = self.mocker.replace('flask.flash')
        mocked_flash(mocker.ANY)

        result_url = 'http://www.mockedurl.com/'
        self._mock_url_for(result_url)
        self._mock_redirect(result_url)

        self.mocker.replay()

        from talks_application.actions import create_talk
        create_talk()

    def tearDown(self):
        self.mocker.restore()
