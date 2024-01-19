from flask import Flask
from user import User

class App():
    """
    Classe principale qui gère les variables du site.
    """

    def __init__(self):
        self.flask_app = Flask(__name__)
        
        # Enlever débugueur quand site en ligne
        self.flask_app.config["DEBUG"] = False

        self.user = User()