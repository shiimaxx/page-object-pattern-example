class AddUserPage(object):

    def __init__(self, driver):
        self.driver = driver

    def add_user(self, username, password):
        user_form = self.driver.find_element_by_id('user_form')
        username_ = user_form.find_element_by_name('username')
        password1 = user_form.find_element_by_name('password1')
        password2 = user_form.find_element_by_name('password2')
        button = user_form.find_element_by_name('_save')
        username_.send_keys(username)
        password1.send_keys(password)
        password2.send_keys(password)
        button.click()
        return UserPage(self.driver)


class UserPage(object):

    def __init__(self, driver):
        self.driver = driver
