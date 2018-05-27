from flask import render_template,redirect,url_for,flash
from flask_login import login_user,login_required,logout_user
from . import auth
from ..models import *
from .forms import RegistrationForm,LoginForm
from ..import db
from ..import bcrypt
from .. import login_manager
from sqlalchemy import exc


@login_manager.user_loader
def load_user(blog_id):
	return Blog.query.get(blog_id)


@auth.route('/login',methods=['GET','POST'])
def login():

	"""this function handles login functionalities"""


	login_form = LoginForm()
	if login_form.validate_on_submit():
		user = Blog.query.filter_by(email=login_form.email.data).first()
		if user and bcrypt.check_password_hash(user.password_hash, login_form.password.data):
			login_user(user,login_form.remember.data)
			flash("succesifull",'success')
			return redirect(url_for('main.index'))
		else:
			print("unsuccessful")
	return render_template('auth/login.html', login_form=login_form)

@auth.route('/register', methods=['GET','POST'])
def register():

	"""this function handles registration functionalities"""
	
	blog_form = RegistrationForm()

	if blog_form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(blog_form.password.data).decode("utf-8")
		user = Blog(name=blog_form.username.data,email=blog_form.email.data,password_hash=hashed_password)
		db.session.add(user)
		db.session.commit()
		# flash("invalid arguments", "danger")
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', blog_form=blog_form)


@auth.route('/logout')
@login_required
def logout():

	"""this function handles logout functionalities"""

	logout_user()
	flash('You have been logged out.',"danger")
	return redirect(url_for('main.index'))
	











































