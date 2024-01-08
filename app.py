import flask

class App():
    """
    Classe principale qui gère les fonctions et les variables du site.
    """

    def __init__(self):
        self.flask_app = flask.Flask(__name__)

        # Enlever débugueur quand site en ligne
        self.flask_app.config["DEBUG"] = True