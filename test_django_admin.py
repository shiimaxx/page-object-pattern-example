import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login import LoginPage


class TestDjangoAdmin(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.set_page_load_timeout(30)
        self.driver.set_window_size(1920, 1080)
        self.driver.get('http://127.0.0.1:8000/admin')

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login('admin', 'p@ssword')

    # def test_search_not_exists_user(self):
    #     pass

    # def test_create_user(self):
    #     pass

    # def test_search_exists_user(self):
    #     pass

    # def test_delete_user(self):
    #     pass

    def tearDown(self):
        self.driver.close()
