from flask_login import UserMixin, AnonymousUserMixin
from . import db
from datetime import datetime

from flask_login import AnonymousUserMixin
from app import login_manager


class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.name = 'Guest'

login_manager.anonymous_user = Anonymous


class User(db.Model,Anonymous):

	""" This model handles the User model that will be mapped to the database"""
	__tablename__="users"

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(255),index=True)
	comment = db.relationship('Comment', backref="user", lazy='dynamic')
	 
	def __repr__(self):
		return f"User : {self.username}"

class Blog(UserMixin,db.Model):

	__tablename__="blog"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), index=True)
	email = db.Column(db.String(200),unique=True)
	bio = db.Column(db.Text)
	pic = db.Column(db.String())
	joined = db.Column(db.DateTime,default=datetime.utcnow)
	password_hash = db.Column(db.String(255))

	post = db.relationship('Post',backref='author',lazy='dynamic')
	comments = db.relationship('Comment',backref='author',lazy='dynamic')
	

class Post(db.Model):
	__tablename__='posts'

	id = db.Column(db.Integer,primary_key=True)
	body = db.Column(db.Text, index=True)
	timestamp=db.Column(db.DateTime,index=True,default=datetime.utcnow)
	blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
	comment = db.relationship('Comment',backref='post', lazy='dynamic')





class Comment(db.Model):
	""" This model handles the Comment model that will be mapped to the database"""

	__tablename__='comments'
	id = db.Column(db.Integer,primary_key=True)
	body = db.Column(db.Text)
	timestamp=db.Column(db.DateTime,index=True,default=datetime.utcnow)

	blog_id= db.Column(db.Integer, db.ForeignKey('blog.id'))

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=True)
	post_id = db.Column(db.Integer, db.ForeignKey('posts.id'),
        nullable=True)

	def __repr__(self):
		return f"Comment : id: {self.id} comment: {self.body}"


class Subscribe(db.Model):
	__tablename__='subscription'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255),)
