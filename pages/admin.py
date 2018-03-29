
class AdminPage():

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://127.0.0.1:8000/admin/'
        self.username = ''
        self.password = ''
