class Users:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role

    def password_matches(self, password):
        return self.password == password
