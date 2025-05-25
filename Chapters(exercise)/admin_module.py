
class User:
    def __init__(self, first_name: str, last_name: str, login_attemps: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attemps

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")

    def greets(self):
        print(f'Hello, {self.first_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
            
class Admin(User):
    def __init__(self, first_name, last_name, login_attemps=0):
        super().__init__(first_name, last_name, login_attemps)
        self.privileges = Privileges()
