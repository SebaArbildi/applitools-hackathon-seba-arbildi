import os

from applitools.common import Region

from applitools.selenium import Eyes
from selenium import webdriver
from unittest_data_provider import data_provider

from traditional_tests.page_objects.login_page_object import LoginPage
from visual_ai_tests.base_ai_test_class import BaseTestClass


class Test02(BaseTestClass):
    def setUp(self):
        self.init()
        self.counter = 0

    def this_init(self):
        self.eyes = Eyes()
        self.eyes.api_key = os.environ['APPLITOOLS_API_KEY']
        self.eyes.batch = self._batch
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.eyes.abort()

    user_password_data = lambda: (
        ('', 'p'), ('u', ''),
        ('', ''), ('u', 'p')
    )

    @data_provider(user_password_data)
    def test_login_errors(self, username, password):
        self.this_init()
        dr = self.eyes.open(self.driver, "Hackathon app", "Test 02: user and password data case: {}".format(self.counter),
                            {'width': 800, 'height': 600})
        self.counter = self.counter + 1
        dr.get(self._url)
        login_page = LoginPage(dr)
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_login_button()
        self.eyes.check_window()
        self.eyes.check_region(Region(left=170, top=280, width=330, height=100))
        self.eyes.close_async()
        self.driver.close()

