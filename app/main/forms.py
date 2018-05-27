from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from wtforms.fields.html5 import EmailField
from wtforms.widgets import Input
from app.models import Subscribe
# from ..models import User

class UpdateProfile(FlaskForm):
	bio = TextAreaField("Tell us about you.", validators=[Required()])
	submit = SubmitField('submit')


class PostForm(FlaskForm):
	body = TextAreaField("whats your pitch ?",validators=[Required()])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	body = TextAreaField('',validators=[Required()])
	submit = SubmitField()

class SubscriptionForm(FlaskForm):
	email = EmailField('Your Email Address',validators=[Required(),Email(message="I don't like your email.")])
	submit = SubmitField('subscribe')

	def validate_email(self, field):
		if Subscribe.query.filter_by(email=field.data).first():
			raise ValidationError('Email already exists.')

class EditPost(FlaskForm):
	body = TextAreaField("update post body.", validators=[Required()])
	submit = SubmitField('submit')
