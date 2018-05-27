from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Server

#local imports
from app import create_app

from app.models import *
from config import *

app = create_app('production')

# manager commands
manager = Manager(app)
migrate = Migrate(app,db)

# manager functionalities
manager.add_command('db',MigrateCommand)
manager.add_command('runserver',Server)

# for shell functionalities.
@manager.shell
def make_shell_context():
	return dict(app=app,db=db)

# testing settings.
@manager.command
def test():
	import unittest
	tests = unittest.TestLoader().discover("tests")
	unittest.TextTestRunner(verbosity=2).run(tests)
if __name__ == '__main__':
	manager.run()