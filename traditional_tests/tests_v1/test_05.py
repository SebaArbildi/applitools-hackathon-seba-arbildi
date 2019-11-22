import unittest

from selenium import webdriver

from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage


class Test05(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://demo.applitools.com/hackathon.html?showAd=true')
        self.login_page = LoginPage(self.driver)
        self.login_page.login('seba', 'seba')

    def tearDown(self):
        self.driver.close()

    def test_dynamic_add(self):
        home_page = HomePage(self.driver)
        flash_sale_present = home_page.flash_sale_is_present()
        flash_sale2_present = home_page.flash_sale2_is_present()
        self.assertTrue(flash_sale_present and flash_sale2_present)