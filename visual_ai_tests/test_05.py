from traditional_tests.page_objects.login_page_object import LoginPage
from visual_ai_tests.base_ai_test_class import BaseTestClass


class Test05(BaseTestClass):

    def setUp(self):
        self.init()
        self.driver.get('https://demo.applitools.com/hackathonV2.html?showAd=true')
        self.login_page = LoginPage(self.driver)
        self.login_page.login('seba', 'seba')

    def tearDown(self):
        self.eyes.abort()
        self.driver.close()

    def test_dynamic_add(self):
        self.eyes.open(self.driver, "Hackathon app", "Dynamic content validation",
                            {'width': 800, 'height': 600})
        self.eyes.check_window()
        self.eyes.close()
