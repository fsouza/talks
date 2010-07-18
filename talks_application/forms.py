from flaskext import wtf
from flaskext.wtf import validators

class TalkForm(wtf.Form):
    title = wtf.TextField('Title', validators=[validators.Required()])
    description = wtf.TextAreaField('Description', validators=[validators.Required()])
    date = wtf.DateField('Date', validators[validators.Required()], format='%m/%d/%Y')
