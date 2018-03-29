
class LoginPage():

    def __init__(self, driver, username, password):
        self.driver = driver
        self.url = 'http://127.0.0.1:8000/admin/login/'
        self.username = username
        self.password = password

    def open(self):
        self.driver.get(self.url)
        return self

    def login(self):
        pass
