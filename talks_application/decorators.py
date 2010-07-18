from google.appengine.api import users
from flask import redirect, url_for

class LoginProtectedAction(object):

    def __init__(self, function):
        self._function = function
        self.__name__ = function.__name__

    def __call__(self, *args, **kwargs):
        try:
            user = users.User()
        except users.UserNotFoundError:
            self._url = url_for(self.__name__, **kwargs)
            return redirect(users.create_login_url(self._url))
        else:
            return self._function(*args, **kwargs)

def login_required(f):
    return LoginProtectedAction(f)
