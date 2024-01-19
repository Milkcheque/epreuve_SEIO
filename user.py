class User():
    """
    Classe qui gère l'utilisateur et ses variables.
    """
    def __init__(self):
        self.is_logged = False
        self.id = ""
        self.pwd = ""

    def set_user_log(self, is_logged:bool):
        """Change la valeur de l'état de connexion de l'utilisateur."""
        self.is_logged = is_logged

    def get_user_log(self):
        """Retourne la valeur de l'état de connexion de l'utilisateur."""
        return self.is_logged