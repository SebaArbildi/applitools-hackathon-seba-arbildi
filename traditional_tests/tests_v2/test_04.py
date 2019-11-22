import time
import unittest

from selenium import webdriver

from traditional_tests.page_objects.chart_page_object import ChartPage
from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage


class Test04(unittest.TestCase):

    # pre-condition to generate original chart, to make comparison on test. If fails, please run it one more time.
    def setUp(self):
        driver = webdriver.Chrome('./chromedriver')
        driver.get('https://demo.applitools.com/hackathonChartV2.html')
        self.wait()
        chartPage = ChartPage(driver)
        chartPage.generate_chart_png('original_2017_2018')
        chartPage.click_show_next_year_button()
        self.wait()
        chartPage.generate_chart_png('original_2019')
        driver.close()

    def test_no_pass_no_username(self):
        driver = webdriver.Chrome('./chromedriver')
        driver.get('https://demo.applitools.com/hackathonV2.html')
        login_page = LoginPage(driver)
        login_page.login('seba', 'seba')
        home_page = HomePage(driver)
        home_page.click_compare_expenses()
        chartPage = ChartPage(driver)
        self.wait()
        chartPage.generate_chart_png('2017_2018_chart')
        valid_2017_2018_chart = chartPage.chart_2017_2018_is_valid('2017_2018_chart')
        self.assertTrue(valid_2017_2018_chart)
        chartPage.click_show_next_year_button()
        self.wait()
        chartPage.generate_chart_png('2019_chart')
        valid_2019_chart = chartPage.chart_2019_is_valid('2019_chart')
        self.assertTrue(valid_2019_chart)

    def wait(self):
        time.sleep(3)
