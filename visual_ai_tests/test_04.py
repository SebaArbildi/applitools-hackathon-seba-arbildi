import os
import unittest

from applitools.selenium import Eyes
from selenium import webdriver

from traditional_tests.page_objects.chart_page_object import ChartPage
from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage


class Test04(unittest.TestCase):

    def setUp(self):
        self.eyes = Eyes()
        self.eyes.api_key = os.environ['APPLITOOLS_API_KEY']

    def tearDown(self):
        self.eyes.abort()

    def test_no_pass_no_username(self):
        driver = webdriver.Chrome('./chromedriver')
        driver.get('https://demo.applitools.com/hackathonV2.html')
        login_page = LoginPage(driver)
        login_page.login('seba', 'seba')
        home_page = HomePage(driver)
        home_page.click_compare_expenses()
        dr = self.eyes.open(driver, "Hackathon app", "Chart validation",
                            {'width': 800, 'height': 600})
        chart_page = ChartPage(dr)
        self.eyes.check_window()
        chart_page.click_show_next_year_button()
        self.eyes.check_window()
        self.eyes.close()
