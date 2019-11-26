import os
import time
import unittest

from applitools.common import BatchInfo
from ddt import ddt, data, unpack

from applitools.selenium import Eyes, Target
from selenium import webdriver
from unittest_data_provider import data_provider

from traditional_tests.page_objects.login_page_object import LoginPage


@ddt
class TestDDTData02(unittest.TestCase):

    def setUp(self):
        self.eyes = Eyes()
        self.eyes.api_key = os.environ['APPLITOOLS_API_KEY']
        self.eyes.batch = BatchInfo('Data Driven Test')
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://demo.applitools.com/hackathon.html') #v1_url
        #self.driver.get('https://demo.applitools.com/hackathonV2.html') #v2_url

    def tearDown(self):
        self.eyes
        self.driver.close()

    user_password_data = lambda: (
        ('',''), ('seba arbildi', '')#,
        #('', 'seba arbildi'), ('seba arbildi', 'seba arbildi')
    )

    @data(('',''), ('a', ''))
    @unpack
    def test_login(self, username, password):
        self.eyes.open(self.driver, "Hackathon app", "test_02_login_data", {'width': 800, 'height': 600})
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(username)
        self.login_page.set_password(password)
        self.login_page.click_login_button()
        self.eyes.check_window()
        self.eyes.close_async()





