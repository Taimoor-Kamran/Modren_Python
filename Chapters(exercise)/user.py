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
