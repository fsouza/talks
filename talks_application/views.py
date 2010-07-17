from talks_application import app

@app.route('/')
def index():
    return 'Hello world'
