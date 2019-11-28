import os
import unittest

from applitools.common import BatchInfo, Region

from applitools.selenium import Eyes
from selenium import webdriver
from unittest_data_provider import data_provider

from traditional_tests.page_objects.login_page_object import LoginPage


class Test02(unittest.TestCase):
    def setUp(self):
        self.batch = BatchInfo('Data Driven Test')
        self.counter = 0
        self.url = 'https://demo.applitools.com/hackathon.html'

    def init(self):
        self.eyes = Eyes()
        self.eyes.api_key = os.environ['APPLITOOLS_API_KEY']
        self.eyes.batch = self.batch
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.eyes.abort()

    user_password_data = lambda: (
        ('', 'p'), ('u', ''),
        ('', '')
    )

    @data_provider(user_password_data)
    def test_login_errors(self, username, password):
        self.init()
        dr = self.eyes.open(self.driver, "Hackathon app", "Test Name: {}".format(self.counter),
                            {'width': 800, 'height': 600})
        self.counter = self.counter + 1
        dr.get(self.url)
        login_page = LoginPage(dr)
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_login_button()
        self.eyes.check_region(Region(left=170, top=280, width=330, height=100))
        self.eyes.close_async()
        self.driver.close()

    def test_login_page_general(self):
        self.init()
        dr = self.eyes.open(self.driver, "Hackathon app", "General element test".format(self.counter),
                            {'width': 800, 'height': 600})
        dr.get(self.url)
        login_page = LoginPage(dr)
        login_page.set_username('username')
        login_page.set_password('')
        login_page.click_login_button()
        self.eyes.check_window()
        self.driver.close()

    def test_login_successful(self):
        self.init()
        dr = self.eyes.open(self.driver, "Hackathon app", "Login successful test".format(self.counter),
                            {'width': 800, 'height': 600})
        dr.get(self.url)
        self.login_page = LoginPage(dr)
        self.login_page.set_username('username')
        self.login_page.set_password('password')
        self.login_page.click_login_button()
        self.eyes.check_window()
        self.driver.close()
