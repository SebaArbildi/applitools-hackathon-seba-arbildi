import unittest

from selenium import webdriver

from traditional_tests.page_objects.login_page_object import LoginPage


class Test01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.close()

    def test_01(self):
        self.driver.get('https://demo.applitools.com/hackathon.html')
        login_page = LoginPage(self.driver)
        login_page.logo_big_img_is_present()
        title = login_page.get_title('Login Form')
        self.assertEqual(title, 'Login Form')
        username = login_page.username_label_is_present()
        self.assertEqual(username, 'Username')
        login_page.get_username_box()
        login_page.username_img_is_present()
        password = login_page.password_label_is_present()
        self.assertEqual(password, 'Password')
        login_page.get_password_box()
        login_page.password_img_is_present()
        login_page.get_login_button()
        login_page.remember_me_button_is_clickeable()
        remember_me = login_page.get_remember_me_label_text()
        self.assertEqual(remember_me.text, 'Remember Me')
        count = login_page.count_social_media_imgs()
        self.assertEqual(count, 3)
