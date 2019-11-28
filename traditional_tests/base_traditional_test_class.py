import time
import unittest

from selenium import webdriver

from traditional_tests.page_objects.chart_page_object import ChartPage


class BaseTestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def wait(self):
        time.sleep(3)

    def generate_original_charts(self):
        driver = webdriver.Chrome('./chromedriver')
        driver.get('https://demo.applitools.com/hackathonChart.html')
        self.wait()
        chartPage = ChartPage(driver)
        chartPage.generate_chart_png('original_2017_2018')
        chartPage.click_show_next_year_button()
        self.wait()
        chartPage.generate_chart_png('original_2019')
        driver.close()
