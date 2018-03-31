from pages.user import AddUserPage, UserPage


class AdminPage():

    def __init__(self, driver):
        self.driver = driver

    def go_to_add_user_page(self):
        self.driver.find_element_by_css_selector('a[href="/admin/auth/user/add/"]').click()
        return AddUserPage(self.driver)
