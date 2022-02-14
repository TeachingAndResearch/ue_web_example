import flask
from database.database import db, init_database
import database.models
from sar2019.config import Config
from sar2019.forms import PostEditForm

app = flask.Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.test_request_context():
    init_database()


@app.route('/')
def index():
    users = database.models.User.query.all()
    return flask.render_template("index.html.jinja2",
                                 users=users)


if __name__ == '__main__':
    app.run()
