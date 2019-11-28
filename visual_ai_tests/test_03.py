import os
import unittest

from applitools.common import Region
from applitools.selenium import Eyes
from selenium import webdriver

from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage


class Test03(unittest.TestCase):

    def setUp(self):
        self.eyes = Eyes()
        self.eyes.api_key = os.environ['APPLITOOLS_API_KEY']

        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://demo.applitools.com/hackathon.html')
        self.login_page = LoginPage(self.driver)
        self.login_page.login('seba', 'seba')

    def tearDown(self):
        self.driver.close()
        self.eyes.abort()

    def test_sort_order_and_data(self):
        dr = self.eyes.open(self.driver, "Hackathon app", "Table Sorting validation",
                            {'width': 800, 'height': 600})
        home_page = HomePage(dr)
        home_page.click_amount_header()
        home_page.scroll_down_to_chart()
        self.eyes.check_window()
        self.eyes.close()

