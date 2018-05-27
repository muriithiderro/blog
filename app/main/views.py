from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import login_required,current_user
from flask.views import View,MethodView
from . import main
from ..models import *
from .forms import *
from .. import db,photos
from .. import socketio,send


class IndexView(View):
	

	def __init__(self,template_name):
		self.template_name = template_name

	def dispatch_request(self):
		self.posts = Post.query.all()
		self.latest_posts = Post.query.order_by(Post.timestamp.desc()).all()

		form = SubscriptionForm()
		if form.validate_on_submit():
			print(form.data)

		
		return render_template(self.template_name, form=form, posts=self.posts, latest_posts=self.latest_posts)

main.add_url_rule('/', view_func=IndexView.as_view('index', template_name='index.html'),methods=["GET","POST"])

class BlogView(MethodView):
	decorators=[login_required,]

	def __init__(self,template_name):
		self.template_name = template_name


	def get(self, uname):
		if uname is None:
			# pass
			abort(404)
		else:
			self.user = Blog.query.filter_by(name=uname).first()
			self.posts = Post.query.filter_by(blog_id=self.user.id).all()
			return render_template(self.template_name, user=self.user,posts=self.posts)


blog_view = BlogView.as_view('blog',template_name="blog/blog.html")
main.add_url_rule('/user/<uname>/', view_func=blog_view)
main.add_url_rule('/user/', defaults={'uname':None}, view_func=blog_view, methods=["GET",])


class PostView(View):
	decorators=[login_required,]

	def __init__(self,template_name):
		self.template_name = template_name

	def dispatch_request(self):
		form = PostForm()
		if form.validate_on_submit():
			post = Post(body=form.body.data, blog_id=current_user.id)
			db.session.add(post)
			db.session.commit()
			return redirect(url_for('main.blog', uname=current_user.name))
		# pitches = Pitch.query.order_by(Pitch.timestamp.desc()).all()

		
		return render_template(self.template_name,form=form)

main.add_url_rule('/post_form', view_func=PostView.as_view('post_form', template_name='post.html'),methods=["GET","POST"])

class PostCommentView(View):

	def __init__(self,template_name):
		self.template_name = template_name

	def dispatch_request(self,id,id2):
		form = CommentForm()
		if form.validate_on_submit():
			comment = Comment(body=form.body.data, blog_id=id, post_id=id2)
			db.session.add(comment)
			db.session.commit()
			return redirect(url_for('main.index', uname=current_user.name, comment=comment))
		

		
		return render_template(self.template_name,form=form)
main.add_url_rule('/comment/<id> && <id2>/', view_func=PostCommentView.as_view('comment', template_name='comment.html'),methods=["GET","POST"])


# comment_view = PostCommentView.as_view('comment',template_name="comment.html")
# main.add_url_rule('/comment/<id>/', view_func=comment_view)
# main.add_url_rule('/comment/', defaults={'id':None}, view_func=comment_view, methods=["GET","POST"])





# class PitchView(View):
# 	decorators=[login_required,]

# 	def __init__(self,template_name):
# 		self.template_name = template_name

# 	def dispatch_request(self,id):
# 		pitch = Pitch.query.get_or_404(id)
# 		form = CommentForm()
# 		if form.validate_on_submit():
# 			comment = Comment(body=form.body.data,pitch=pitch,author=current_user._get_current_object())
			
# 			db.session.add(comment)
# 			db.session.commit()
# 			flash('your comment has been added','success')
# 			return redirect(url_for('main.index',id=pitch.id))
# 		comments = Comment.query.filter_by(pitch_id=id).all()
# 		user = User.query.filter_by(id=Comment.author_id).first()

	
# 		return render_template(self.template_name,form=form,pitch=pitch,comments=comments,user=user)

# main.add_url_rule('/pitch/<int:id>/', view_func=PitchView.as_view('pitch', template_name='pitch.html'),methods=["GET","POST"])


@main.route('/user/<id>/post', methods=['GET', 'POST'])
@login_required
def edit_post(id):
	form = EditPost()
	if form.validate_on_submit():
		post = Post.query.filter_by(id=id).first()
		post.body = form.body.data
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('main.blog',uname=current_user.name))
	return render_template('blog/post_update.html', form=form)

@main.route('/user/<id>/comments', methods=['GET', 'POST'])

def comments(id):
	post = Post.query.filter_by(id=id).first()

	return render_template('all_comments.html', post=post)


@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_blog(uname):
	user = Blog.query.filter_by(name=uname).first()
	if user is None:
		abort(404)

	form = UpdateProfile()
	if form.validate_on_submit():
		user.bio = form.bio.data

		db.session.add(user)
		db.session.commit()

		return redirect(url_for('main.blog',uname=user.name))
	return render_template('blog/update.html', form=form)


@main.route('/user/<uname>/upadate/pic',methods=['GET','POST'])
@login_required
def update_pic(uname):
	user = Blog.query.filter_by(name=uname).first()
	if 'photo' in request.files:
		filename = photos.save(request.files['photo'])
		path = f"photos/{filename}"
		user.pic=path
		db.session.commit()
	return redirect(url_for('main.blog',uname=uname))

@main.route('/delete/<int:id>')
def delete(id):
	post = Post.query.filter_by(id=id).first()
	db.session.delete(post)
	db.session.commit()
	return redirect(url_for('main.blog', uname=current_user.name))

@main.route('/delete/<id>/comment')
def delete_comment(id):
	comment = Comment.query.filter_by(id=id).first()
	db.session.delete(comment)
	db.session.commit()
	return redirect(url_for('main.comments', id=comment.post_id))


@main.app_errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@main.app_errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500




