import os
import unittest

from applitools.common import BatchInfo, Region
from applitools.selenium import Eyes
from unittest_data_provider import data_provider

from traditional_tests.page_objects.chart_page_object import ChartPage
from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage
from selenium import webdriver


class TestsVisualAI(unittest.TestCase):
    _batch = BatchInfo('Hackathon')
    _url = 'https://demo.applitools.com/hackathonV2.html'

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.eyes = Eyes()
        self.eyes.api_key = os.environ['APPLITOOLS_API_KEY']
        self.eyes.batch = self._batch
        self.driver.get(self._url)

    def tearDown(self):
        self.eyes.abort()
        self.driver.close()

    def test_01_elements_presence_on_login_page(self):
        self.eyes.open(self.driver, "Hackathon app", "Test 01: elements presence", {'width': 800, 'height': 600})
        self.eyes.check_window()
        self.eyes.close()

    user_password_data = lambda: (
        ('', 'p'), ('u', ''),
        ('', ''), ('u', 'p')
    )

    @data_provider(user_password_data)
    def test_02_login_errors(self, username, password):
        self.setUp()
        dr = self.eyes.open(self.driver, "Hackathon app",
                            "Test 02: user={} and password={}".format(username, password),
                            {'width': 800, 'height': 600})
        dr.get(self._url)
        login_page = LoginPage(dr)
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_login_button()
        self.eyes.check_window()
        self.eyes.check_region(Region(left=170, top=280, width=350, height=100))
        self.eyes.close_async()

    def test_03_sort_order_and_data(self):
        login_page = LoginPage(self.driver)
        login_page.login('seba', 'seba')
        dr = self.eyes.open(self.driver, "Hackathon app", "Test 03: Table Sorting validation",
                            {'width': 800, 'height': 600})
        home_page = HomePage(dr)
        home_page.click_amount_header()
        home_page.scroll_down_to_chart()
        self.eyes.check_window()
        self.eyes.close()

    def test_04_chart_validation(self):
        login_page = LoginPage(self.driver)
        login_page.login('seba', 'seba')
        home_page = HomePage(self.driver)
        home_page.click_compare_expenses()
        dr = self.eyes.open(self.driver, "Hackathon app", "Test 04: Chart validation",
                            {'width': 800, 'height': 600})
        chart_page = ChartPage(dr)
        self.eyes.check_window()
        chart_page.click_show_next_year_button()
        self.eyes.check_window()
        self.eyes.close()

    def test_05_dynamic_add(self):
        self.driver.get('https://demo.applitools.com/hackathonV2.html?showAd=true')
        login_page = LoginPage(self.driver)
        login_page.login('seba', 'seba')
        self.eyes.open(self.driver, "Hackathon app", "Test 05: Dynamic content validation",
                            {'width': 800, 'height': 600})
        self.eyes.check_window()
        self.eyes.close()

