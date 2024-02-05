from flask import Flask
import flask
from database.database import db, init_database
import database.models
from utilities.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.test_request_context():
    init_database()


def get_all_engineers():
    return database.models.Engineer.query.all()


def get_engineer_by_id(engineer_id):
    return database.models.Engineer.query.filter_by(id=engineer_id).first()


def get_engineers_in_site(site_name):
    return database.models.Engineer.query.filter_by(site=site_name).all()


@app.route('/')
def index():
    engineers = get_all_engineers()

    result = "All engineers:\n"

    for engineer in engineers:
        result += " - %s (id:%s)\n" % (engineer.username, engineer.id)

    return flask.Response(result,
                          mimetype="text")


@app.route('/engineer/id/<int:engineer_id>')
def show_engineer_by_id(engineer_id):
    return "TODO: codez moi!"


if __name__ == '__main__':
    app.run()
