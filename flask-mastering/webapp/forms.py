import wtforms
import re
from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class CustomEmail(object):
    def __init__(self, message="fuck"):
        self.message = message

    def __call__(self, form, field):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", field.data):
            raise wtforms.ValidationError("Field must be a valid email address")


class CommentForm(Form):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=3)]
    )
    text = TextAreaField(u'Comment', validators=[DataRequired()])
    email = TextAreaField(u'Email', validators=[CustomEmail()])
