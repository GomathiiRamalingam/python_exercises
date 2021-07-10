class User():
    def __init__(self, first_name, last_name, username, password, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.login_attempts = login_attempts

    def describe_user(self):
        print('\nFull Name: ' + self.first_name.title(), self.last_name.title())
        print('Username: ', self.username)
        print('Password: ',self.password)

    def greet_user(self):
        print('Welcome back to the heel :)')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('ricardo', 'santos', 'riikcsantos', 'ricardin123')
user2 = User('sabrina', 'maldaner', 'brina', 'brina9302193')
user3 = User('caique', 'oliveira', 'caciquis', 'caiquem123')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

login_test = User('login', 'attempt', 'admin', '1234')
print(login_test.login_attempts)
login_test.increment_login_attempts()
login_test.increment_login_attempts()
login_test.increment_login_attempts()
login_test.increment_login_attempts()
login_test.increment_login_attempts()
print(login_test.login_attempts)
login_test.reset_login_attempts()
print(login_test.login_attempts)

