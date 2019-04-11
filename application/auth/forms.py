from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Your name", [validators.Length(min=2, max=32, message="Name must be 2-32 characters long")])
    username = StringField("Username", [validators.Length(min=2, max=32, message="Username must be 2-32 characters long")])
    password = PasswordField("Password", [validators.Length(min=6, message="Password must be at least 6 characters long")])

    class Meta:
        csrf = False