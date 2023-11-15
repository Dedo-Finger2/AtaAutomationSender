class Auth:
    email, password = None, None

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

