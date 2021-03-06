from flask import Flask, redirect, url_for
from config import DevConfig
from models import db, mongo, Reminder
from controllers.blog import blog_blueprint
from controllers.main import main_blueprint
from extensions import bcrypt, celery
from sqlalchemy import event
from .tasks import on_reminder_save


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)
    mongo.init_app(app)
    bcrypt.init_app(app)
    celery.init_app(app)
    event.listen(Reminder, 'after_insert', on_reminder_save)

    @app.route('/')
    def index():
        return redirect(url_for('blog.home'))

    app.register_blueprint(blog_blueprint)
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app.run()
