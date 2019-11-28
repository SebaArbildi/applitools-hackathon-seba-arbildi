import time
import unittest

from selenium import webdriver

from traditional_tests.base_traditional_test_class import BaseTestClass
from traditional_tests.page_objects.chart_page_object import ChartPage
from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage


class Test04(BaseTestClass):

    # pre-condition to generate original chart, to make comparison on test. If fails, please run it one more time.
    def setUp(self):
        self.generate_original_charts()
        self.init_driver()
        self.driver.get('https://demo.applitools.com/hackathonV2.html')
        login_page = LoginPage(self.driver)
        login_page.login('seba', 'seba')
        home_page = HomePage(self.driver)
        home_page.click_compare_expenses()
        self.chartPage = ChartPage(self.driver)

    def test_2017_2018_charts_validation(self):
        self.wait()
        self.chartPage.generate_chart_png('2017_2018_chart')
        valid_2017_2018_chart = self.chartPage.chart_2017_2018_is_valid('2017_2018_chart')
        self.assertTrue(valid_2017_2018_chart, 'To see differences, look ./tmp/result_2017_2018.png')

    def test_2019_charts_validation(self):
        self.chartPage.click_show_next_year_button()
        self.wait()
        self.chartPage.generate_chart_png('2019_chart')
        valid_2019_chart = self.chartPage.chart_2019_is_valid('2019_chart')
        self.assertTrue(valid_2019_chart, 'To see differences, look ./tmp/result_2019.png')

