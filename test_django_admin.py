import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDjangoAdmin(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=options)

    def test_login(self):
        pass

    def test_search_not_exists_user(self):
        pass

    def test_create_user(self):
        pass

    def test_search_exists_user(self):
        pass

    def test_delete_user(self):
        pass
