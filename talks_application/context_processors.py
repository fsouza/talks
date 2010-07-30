from google.appengine.api.users import create_login_url, create_logout_url
from talks_application import app

@app.context_processor
def inject_login_url():
    return dict(create_login_url=create_login_url, create_logout_url=create_logout_url)
