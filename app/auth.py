class AuthManager:
    def __init__(self):
        self.admin_password = "Sreenath@123"

    def verify(self, password):
        return password == self.admin_password
    