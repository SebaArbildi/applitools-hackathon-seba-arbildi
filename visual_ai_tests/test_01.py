import os
import unittest

from selenium import webdriver
from applitools.selenium import Eyes, Target


from traditional_tests.page_objects.login_page_object import LoginPage


class Test01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.eyes = Eyes()
        self.eyes.api_key = os.environ['APPLITOOLS_API_KEY']
        self.eyes.open(self.driver, "Hackathon app", "test_01_elements_presence", {'width': 800, 'height': 600})
        self.driver.get('https://demo.applitools.com/hackathon.html')
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()
        self.eyes.abort()

    def test_elements_presence_on_login_page(self):
        self.eyes.check_window()
        self.eyes.close()


