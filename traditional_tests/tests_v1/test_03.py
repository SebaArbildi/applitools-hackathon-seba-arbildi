from traditional_tests.base_traditional_test_class import BaseTestClass
from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage


class Test03(BaseTestClass):

    def setUp(self):
        self.init_driver()
        self.driver.get('https://demo.applitools.com/hackathon.html')
        self.login_page = LoginPage(self.driver)
        self.login_page.login('seba', 'seba')
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_valid_amount_order_after_sort(self):
        original_table = self.home_page.get_transactions_table()
        amount_original = self.home_page.get_amount_order(original_table)
        amount_original.sort()
        self.home_page.click_amount_header()
        new_table = self.home_page.get_transactions_table()
        amount_new = self.home_page.get_amount_order(new_table)
        valid_amount_order = self.home_page.validate_amount_order(amount_original, amount_new)
        self.assertTrue(valid_amount_order)

    def test_valid_data_after_sort(self):
        original_table = self.home_page.get_transactions_table()
        self.home_page.click_amount_header()
        new_table = self.home_page.get_transactions_table()
        valid_data = self.home_page.validate_table_data(original_table, new_table)
        self.assertTrue(valid_data)



