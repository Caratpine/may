from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from webapp import create_app
from webapp.config import DevConfig
from webapp.models import db, User, Post, Tag, Comment, Reminder

app = create_app(DevConfig)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app,
                db=db,
                User=User,
                Post=Post,
                Tag=Tag,
                Comment=Comment,
                Reminder=Reminder
                )

if __name__ == '__main__':
    manager.run()
