from traditional_tests.base_traditional_test_class import BaseTestClass
from traditional_tests.page_objects.login_page_object import LoginPage


class Test01(BaseTestClass):

    def setUp(self):
        self.init_driver()
        self.driver.get('https://demo.applitools.com/hackathonV2.html')
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_logo_big_img_is_present(self):
        element = self.login_page.logo_big_img_is_present()
        self.assertIsNotNone(element)

    #Issue: AssertionError: 'Logout Form' != 'Login Form'
    def test_title_is_login_form(self):
        title = self.login_page.get_title('Login Form')
        self.assertIsNotNone(title)
        self.assertEqual('Login Form', title, 'Issue: Actual:Logout Form. Expected: Login Form')

    def test_username_label_is_present(self):
        username = self.login_page.username_label_is_present()
        self.assertIsNotNone(username)
        self.assertEqual('Username', username)

    def test_username_box_is_present(self):
        element = self.login_page.get_username_box()
        self.assertIsNotNone(element)

    #Issue: username image is not present
    def test_username_img_is_present(self):
        element = self.login_page.username_img_is_present()
        self.assertIsNotNone(element, 'Issue: username image is not present')

    #Issue: Password != Pwd
    def test_password_label_is_present(self):
        password = self.login_page.password_label_is_present()
        self.assertIsNotNone(password)
        self.assertEqual('Password', password, 'Issue: Password != Pwd')

    def test_password_box_is_present(self):
        element = self.login_page.get_password_box()
        self.assertIsNotNone(element)

    #Issue: password img is not present
    def test_password_img_is_present(self):
        element = self.login_page.password_img_is_present()
        self.assertIsNotNone(element, 'Issue: password img is not present')

    def test_get_login_button(self):
        element = self.login_page.get_login_button()
        self.assertIsNotNone(element)

    def test_remember_me_button_is_clickable(self):
        element = self.login_page.remember_me_button_is_clickable()
        self.assertIsNotNone(element)

    def test_get_remember_me_label_text(self):
        remember_me = self.login_page.get_remember_me_label_text()
        self.assertEqual('Remember Me', remember_me.text)

    #Missing Linkedin Media img
    def test_count_social_media_imgs(self):
        count = self.login_page.count_social_media_imgs_v2()
        self.assertEqual(3, count, 'Missing Linkedin Media img')

