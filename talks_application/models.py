from google.appengine.ext import db

class Talk(db.Model):
    title = db.StringProperty(required=True)
    description = db.StringProperty(required=True, multiline=True)
    date = db.DateTimeProperty(required=True)
    presented_by = db.UserProperty(required=True)
