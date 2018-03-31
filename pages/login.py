from pages.admin import AdminPage


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        login_form = self.driver.find_element_by_id('login-form')
        username_ = login_form.find_element_by_name('username')
        password_ = login_form.find_element_by_name('password')
        button = login_form.find_element_by_css_selector('input[value="ログイン"]')
        username_.send_keys(username)
        password_.send_keys(password)
        button.click()
        return AdminPage(self.driver)
