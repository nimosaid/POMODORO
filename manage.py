from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Pitch, Category, Vote, Comment
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('production')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server',Server)
manager.add_command('db', MigrateCommand)

manager.add_command('server',Server)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
   
if __name__ == '__main__':
    manager.run()