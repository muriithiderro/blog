# Blog Application.

 The Blog App allows a user to view and comment posts on my blog, for a writter can also register and start posting posts that will be commented by other users, the user can also subscribe to the app to be informed of a new post via their email.
#### By **Derrick** created on, May 26th 2018 

## Description

This Application is python based and runs on any browser, It allows a user to view and comment posts on my blog, for a writter can also register and start posting posts that will be commented by other users, the user can also subscribe to the app to be informed of a new post via their email, a writter can publish new posts, comment them, delete posts and comments on the posts he/she created.

## Behaviour of the application

### Authentication

+ Once the url is entered at the browser, the user gets the landing page that has all the posts, the user can comment on the various posts, view all recent posts and subscribe.
+ For a Writter he can create a personal blog by registering and login. 
- If the user is anonymouse, He/she can only view posts, comment and subscribe.
- If the writter on the the other hand is Authnticated but logged out, can login again to interact with the app by entering email and password details into a form.
- The user last option is to register using a unique username and a password after which the user is redirected to login to the app.
- Once the user is authenticated, can logout at will.

### Posts.

+ The Writter Can add Posts and they get displayed from the most resent one.
+ The post information is displayed alongside other posts, a post contains information such as post body, post author and the time of creation.
+ On the sidebar the user can see the most recent post.

### Subscription

+ Any user who visits the site can subscribe by submitting his/her desired email via the subscription form.

### Blog
+ The writter can also writter can also edit ther blog, post a new post, delete a post and any comment associated with it.

## Development and Setup.

### prerequisites
+ First clone the project to your camputer. ```git clone <repo url>```
+ Ensure python3 is installed.
+ Install virtual environment by running ```pip3 install virtualenv```
+ Create a virtualenvironment by running ``` virtualenv <name of environment>``` on the terminal and once its activated by running ``` source <name of environment>/bin/activate``` then install all the packages by running ```pip3 install -r requirements.txt```
+ Then start the server by running ```python3 manage.py runserver```.
+ Copy the link and paste in any browser ```http://localhost:5000```


### Important packages used in app development.

```
certifi==2018.4.16
chardet==3.0.4
click==6.7
dominate==2.3.1
Flask==1.0.2
Flask-Bootstrap4==4.0.2
Flask-Script==2.0.6
Flask-SQLAlchemy==2.3.2
idna==2.6
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
requests==2.18.4
visitor==0.1.3
Werkzeug==0.14.1

```

## Technology and Tools Used

+ Python3.6 - Programming language
- Flask - Python micro-framework
- Git - Version control
- Sublime text - Code editor
- Postgres - Database

## Test Driven Development

Testing was done using python inbuild test tool called **unittest** to test database connections ,forms and models.

## Further help
To get Further help you can visit the official [python](https://www.python.org/) and [flask](http://flask.pocoo.org/ ) documentation.

## Licence
MIT (c) 2017 [muriithi derrick](https://github.com/muriithiderro)
