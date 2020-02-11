import flask
from sar2019.config import Config


app = flask.Flask(__name__)
app.config.from_object(Config)


def traitement_formulaire_addition(form):
    expression = f"{form.get('number_a')} {form.get('operator')} {form.get('number_b')}"
    resultat = "%s" % eval(expression)
    return resultat


def afficher_formulaire_addition(form):
    return flask.render_template("form_addition.html.jinja2")


@app.route("/add", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def fonction_formulaire_addition():

    number_a = flask.request.form.get("number_a")
    number_b = flask.request.form.get("number_b")
    operator = flask.request.form.get("operator")

    if number_a is None or number_b is None or operator is None:
        return afficher_formulaire_addition(flask.request.form)
    else:
        return traitement_formulaire_addition(flask.request.form)


if __name__ == '__main__':
    app.run(debug=True)
