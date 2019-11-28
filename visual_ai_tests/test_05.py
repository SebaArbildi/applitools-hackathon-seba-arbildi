import os
import unittest

from applitools.selenium import Eyes
from selenium import webdriver

from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage


class Test05(unittest.TestCase):

    def setUp(self):
        self.eyes = Eyes()
        self.eyes.api_key = os.environ['APPLITOOLS_API_KEY']
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://demo.applitools.com/hackathonV2.html?showAd=true')
        self.login_page = LoginPage(self.driver)
        self.login_page.login('seba', 'seba')

    def tearDown(self):
        self.eyes.abort()
        self.driver.close()

    def test_dynamic_add(self):
        self.eyes.open(self.driver, "Hackathon app", "Dynamic content validation",
                            {'width': 800, 'height': 600})
        self.eyes.check_window()
        self.eyes.close()
