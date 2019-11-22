import unittest

from selenium import webdriver

from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage


class Test03(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://demo.applitools.com/hackathon.html')
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_table_sort_test(self):
        self.login_page.login('seba', 'seba')
        home_page = HomePage(self.driver)

        original_table = home_page.get_transactions_table()
        amount_original = home_page.get_amount_order(original_table)
        amount_original.sort()

        home_page.click_amount_header()

        new_table = home_page.get_transactions_table()
        amount_new = home_page.get_amount_order(new_table)

        valid_amount_order = home_page.validate_amount_order(amount_original, amount_new)
        valid_data = home_page.validate_table_data(original_table, new_table)
        self.assertTrue(valid_amount_order and valid_data)


