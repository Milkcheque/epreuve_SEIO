

class User():
    def __init__(self):
        self.is_logged = False
        self.id = ""
        self.pwd = ""

    def set_user_log(self, is_logged):
        self.is_logged = is_logged

    def get_user_log(self):
        return self.is_logged