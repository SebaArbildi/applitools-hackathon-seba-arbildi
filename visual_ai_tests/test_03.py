import os
import unittest

from applitools.common import BatchInfo

from applitools.selenium import Eyes, Target
from selenium import webdriver
from unittest_data_provider import data_provider

from traditional_tests.page_objects.login_page_object import LoginPage


class TestDDTData02(unittest.TestCase):
    def setUp(self):
        self.batch = BatchInfo('Data Driven Test')
        self.counter = 0

    def init(self):
        self.eyes = Eyes()
        self.eyes.api_key = os.environ['APPLITOOLS_API_KEY']
        self.eyes.batch = self.batch
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.eyes.abort()

    user_password_data = lambda: (
        ('','p'), ('u', ''),
        ('', ''), ('u', 'p')
    )

    @data_provider(user_password_data)
    def test_login(self, username, password):
        self.init()
        dr = self.eyes.open(self.driver, "Hackathon app", "Test Name: {}".format(self.counter), {'width': 800, 'height': 600})
        self.counter = self.counter + 1
        dr.get('https://demo.applitools.com/hackathonV2.html')
        self.login_page = LoginPage(dr)
        self.login_page.set_username(username)
        self.login_page.set_password(password)
        self.login_page.click_login_button()
        self.eyes.check_window()
        self.eyes.close_async()
        self.driver.close()
