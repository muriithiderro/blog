import unittest
from flask_testing import TestCase
from app import bcrypt
from app import db
from app.models import *
from datetime import datetime
from app.auth.forms import RegistrationForm,LoginForm

class TestBlog(unittest.TestCase):
	"""The class that handles Blog model testing"""

	def setUp(self):
		"""this method definines initiation of the data used for testing,
		 its run before testing begins"""

		self.hashed_password = bcrypt.generate_password_hash('secrets').decode("utf-8")
		self.blog_derrick = Blog(name="derrick",password_hash=self.hashed_password,email="derrick@gmail.com",joined=datetime.utcnow(),pic="/path/to/picture")
	def tearDown(self):
		Blog.query.delete()
		
	def test_check_instance_variables(self):
		"""testing whether instantiation is properly done"""

		self.assertEquals(self.blog_derrick.name,'derrick')
		self.assertEquals(self.blog_derrick.email, 'derrick@gmail.com')


	def test_harshing(self):
		"""this method checks instantiation of password hashes"""

		self.assertTrue(bcrypt.check_password_hash(self.blog_derrick.password_hash, 'secrets'))

	def test_save_blog(self):
		"""this method tests whether users are properly saved in the databse"""

		db.session.add(self.blog_derrick)
		db.session.commit()
		self.assertTrue(len(Blog.query.all())>0)

	def test_whether_data_is_saved(self):
		"""this method checks proper retrieval of data"""

		db.session.add(self.blog_derrick)
		db.session.commit()
		blog = Blog.query.filter_by(name=self.blog_derrick.name).first()
		self.assertEquals(self.blog_derrick.name,blog.name)

	

class TestPost(unittest.TestCase):
	"""The class that handles post model testing"""

	def setUp(self):
		self.post = Post(body="cool friday",blog_id=33,timestamp=datetime.utcnow())

	def tearDown(self):
		pass
		# Post.query.delete()

	def test_check_post_instance_variables(self):
		"""testing whether instantiation is properly done"""

		self.assertEquals(self.post.body,"cool friday")

	def test_save_post(self):
		"""this method tests whether posts are properly saved in the databse"""
		db.session.add(self.post)
	
		db.session.commit()
		self.assertTrue(len(Post.query.all())>0)

	def test_whether_posr_data_is_saved(self):
		"""this method checks proper retrieval of data"""

		db.session.add(self.post)
		db.session.commit()
		post = Post.query.filter_by(body=self.post.body).first()
		self.assertEquals(self.post.body,post.body)

class TestComment(unittest.TestCase):
	"""The class that handles comment model testing"""

	def setUp(self):
		self.comment = Comment(blog_id=25,body="nyce one",timestamp=datetime.utcnow())

	def tearDown(self):
		"""this method is done after the tests"""

		Comment.query.delete()

	def test_check_comment_instance_variables(self):
		"""testing whether instantiation is properly done"""

		self.assertEquals(self.comment.body,"nyce one")
		self.assertEquals(self.comment.blog_id, 33)

	def test_save_comment(self):
		"""this method tests whether comments are properly saved in the databse"""

		db.session.add(self.comment)
		db.session.commit()
		self.assertTrue(len(Comment.query.all())>0)

	def test_whether_comment_data_is_saved(self):
		"""this method checks proper retrieval of data"""

		db.session.add(self.comment)
		db.session.commit()
		comment = Comment.query.filter_by(blog_id=self.comment.blog).first()
		self.assertEquals(self.comment.blog_id,comment.blog_id)


class TestRegistrationForm(unittest.TestCase):
	"""This class handles tests for registation form model"""

	def setUp(self):
		"""this method is for data initialization for tests"""

		self.new_form = RegistrationForm(email="admin@gmail.com",username="Admin",password="secret",password_confirm="secret")

	def test_registration(self):
		"""This method tests initialization of registration form instances"""

		# print(self.new_form.data)

		self.assertEquals(self.new_form.data['username'],'Admin')
		self.assertEquals(self.new_form.data['submit'],False)

class TestLoginForm(unittest.TestCase):
	"""This class handles tests for registation form model"""

	def setUp(self):
		"""this method is for data initialization for tests"""

		self.new_form = LoginForm(email="admin@gmail.com",password="secret",remember=True)

	def test_login_form(self):
		"""This method tests initialization of login form instances"""

		self.assertEquals(self.new_form.data['email'],'admin@gmail.com')
		self.assertEquals(self.new_form.data['password'],"secret")
		self.assertEquals(self.new_form.data['remember'],True)