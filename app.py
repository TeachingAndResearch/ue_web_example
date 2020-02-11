import flask
from sar2019.config import Config


app = flask.Flask(__name__)
app.config.from_object(Config)


def traitement_formulaire_addition(form):
    expression = f"{form.get('number_a')} {form.get('operator')} {form.get('number_b')}"
    resultat = "%s" % eval(expression)
    return resultat


def afficher_formulaire_addition(form, errors):
    return flask.render_template("form_addition.html.jinja2")


def formulaire_est_valide(form):
    number_a = flask.request.form.get("number_a")
    number_b = flask.request.form.get("number_b")
    operator = flask.request.form.get("operator")

    result = True
    errors = []

    if number_a is None:
        result = False
        errors += ["missing 'number_a' parameter"]
    if number_b is None:
        result = False
        errors += ["missing 'number_b' parameter"]
    if operator is None:
        result = False
        errors += ["missing 'operator' parameter"]

    return result, errors


@app.route("/add", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def fonction_formulaire_addition():

    form_est_valide, errors = formulaire_est_valide(flask.request.form)

    if not form_est_valide:
        return afficher_formulaire_addition(flask.request.form, errors)
    else:
        return traitement_formulaire_addition(flask.request.form)


if __name__ == '__main__':
    app.run(debug=True)
