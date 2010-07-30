from google.appengine.api import users
from talks_application import app

@app.context_processor
def inject_login_url():
    return dict(create_login_url=users.create_login_url, create_logout_url=users.create_logout_url)

@app.context_processor
def inject_user():
    try:
        user = users.User()
    except users.UserNotFoundError:
        user = None
    return {'user' : user}
