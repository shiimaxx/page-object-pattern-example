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

    def test_add_user(self):
        self.driver.get('http://127.0.0.1:8000/admin')
        login_page = LoginPage(self.driver)
        admin_page = login_page.login('admin', 'p@ssword')
        add_user_page = admin_page.go_to_add_user_page()
        change_user_page = add_user_page.add_user('testuser', 'dummy_p@ssword')
        self.assertIn('testuser</a>" を追加しました。続けて編集できます。</li>', change_user_page.driver.page_source)

    def tearDown(self):
        self.driver.close()
