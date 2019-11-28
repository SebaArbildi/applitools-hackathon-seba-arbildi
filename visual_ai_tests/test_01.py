from traditional_tests.page_objects.login_page_object import LoginPage
from visual_ai_tests.base_ai_test_class import BaseTestClass


class Test01(BaseTestClass):

    def setUp(self):
        self.init()

    def tearDown(self):
        self.driver.close()
        self.eyes.abort()

    def test_elements_presence_on_login_page(self):
        self.eyes.open(self.driver, "Hackathon app", "test_01_elements_presence", {'width': 800, 'height': 600})
        self.login_page = LoginPage(self.driver)
        self.eyes.check_window()
        self.eyes.close()


