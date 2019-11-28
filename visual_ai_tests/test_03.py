from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage
from visual_ai_tests.base_ai_test_class import BaseTestClass


class Test03(BaseTestClass):

    def setUp(self):
        self.init()
        self.login_page = LoginPage(self.driver)
        self.login_page.login('seba', 'seba')

    def tearDown(self):
        self.driver.close()
        self.eyes.abort()

    def test_sort_order_and_data(self):
        dr = self.eyes.open(self.driver, "Hackathon app", "Test 03: Table Sorting validation",
                            {'width': 800, 'height': 600})
        home_page = HomePage(dr)
        home_page.click_amount_header()
        home_page.scroll_down_to_chart()
        self.eyes.check_window()
        self.eyes.close()

