from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User
from wtforms.fields.html5 import EmailField

class RegistrationForm(FlaskForm):
    email = EmailField('Your Email Address',validators=[Required(),Email(message="I don't like your email.")])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('Your Email Address', validators=[Required(),Email()])
	password = PasswordField('Password', validators=[Required()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Sign In')