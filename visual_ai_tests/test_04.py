from traditional_tests.page_objects.chart_page_object import ChartPage
from traditional_tests.page_objects.home_page_object import HomePage
from traditional_tests.page_objects.login_page_object import LoginPage
from visual_ai_tests.base_ai_test_class import BaseTestClass


class Test04(BaseTestClass):

    def setUp(self):
        self.init()

    def tearDown(self):
        self.eyes.abort()

    def test_no_pass_no_username(self):
        login_page = LoginPage(self.driver)
        login_page.login('seba', 'seba')
        home_page = HomePage(self.driver)
        home_page.click_compare_expenses()
        dr = self.eyes.open(self.driver, "Hackathon app", "Chart validation",
                            {'width': 800, 'height': 600})
        chart_page = ChartPage(dr)
        self.eyes.check_window()
        chart_page.click_show_next_year_button()
        self.eyes.check_window()
        self.eyes.close()
