
class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        return self

    def login(self, username, password):
        login_form = self.driver.find_element_by_id('login-form')
        id_ = login_form.find_element_by_name('username')
        pw = login_form.find_element_by_name('password')
        button = login_form.find_element_by_css_selector('input[value="ログイン"]')
        id_.send_keys(username)
        pw.send_keys(password)
        button.click()
        return self
