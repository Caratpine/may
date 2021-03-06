import wtforms
import re
from flask_wtf import Form
from wtforms import (
    StringField,
    TextAreaField,
    PasswordField,
    BooleanField
)
from wtforms.validators import DataRequired, Length, EqualTo, URL
from models import User


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
    # email = TextAreaField(u'Email', validators=[CustomEmail()])


class LoginForm(Form):
    username = StringField('Username', [
        DataRequired(), Length(max=255)
    ])
    password = PasswordField('Password', [DataRequired()])

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        if not check_validate:
            return False

        user = User.query.filter_by(
            username=self.username.data
        ).first()

        if not user:
            self.username.errors.append(
                'Invalid username or password'
            )
            return False

        if not user.check_password(self.password.data):
            self.username.errors.append(
                'Invalid username or password'
            )
            return False
        return True


class RegisterForm(Form):
    username = StringField('Username', [
        DataRequired(),
        Length(max=255)
    ])
    password = PasswordField('Password', [
        DataRequired(),
        Length(min=8)
    ])
    confirm = PasswordField('confirm Password', [
        DataRequired(),
        EqualTo('password')
    ])

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        if not check_validate:
            return False

        user = User.query.filter_by(
            username=self.username.data
        ).first()

        if user:
            self.username.errors.append(
                "User with that name already exists"
            )
            return False
        return True


class PostForm(Form):
    title = StringField('Title', [
        DataRequired(),
        Length(max=255)
    ])
    text = TextAreaField('Content', [DataRequired()])
