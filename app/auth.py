class AuthManager:
    def __init__(self):
        self.admin_password = "admin123"

    def verify(self, password):
        return password == self.admin_password
    