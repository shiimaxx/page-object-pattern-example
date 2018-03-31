class AddUserPage(object):

    def __init__(self, driver):
        self.driver = driver

    def add_user(self, username, password):
        login_form = self.driver.find_element_by_id('user_form')
        username_ = login_form.find_element_by_name('username')
        password1 = login_form.find_element_by_name('password1')
        password2 = login_form.find_element_by_name('password2')
        button = login_form.find_element_by_name('_save')
        username_.send_keys(username)
        password1.send_keys(password)
        password2.send_keys(password)
        button.click()
        return ChangeUserPage(self.driver)


class ChangeUserPage(object):

    def __init__(self, driver):
        self.driver = driver
