import unittest

from selenium import webdriver

from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage


class Test02(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://demo.applitools.com/hackathon.html')
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_no_pass_no_username(self):
        self.login_page.click_login_button()
        warning_msg = self.login_page.get_warning_msg()
        self.assertEqual('Both Username and Password must be present', warning_msg)

    def test_no_pass_yes_username(self):
        self.login_page.set_username('seba arbildi')
        self.login_page.click_login_button()
        warning_msg = self.login_page.get_warning_msg()
        self.assertEqual('Password must be present', warning_msg)

    def test_yes_pass_no_username(self):
        self.login_page.set_password('seba arbildi')
        self.login_page.click_login_button()
        warning_msg = self.login_page.get_warning_msg()
        self.assertEqual('Username must be present', warning_msg)

    def test_valid_pass_valid_username(self):
        self.login_page.set_username('seba arbildi')
        self.login_page.set_password('seba arbildi')
        self.login_page.click_login_button()
        home_page = HomePage(self.driver)
        self.assertIsNotNone(home_page.user_is_logged_in())


