
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from traditional_tests.page_objects.utils import Utils


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def logo_big_img_is_present(self):
        return Utils.wait_presence_and_get_element(self.driver, By.CSS_SELECTOR, '.logo-w img')

    def get_title(self, title):
        element = Utils.wait_presence_and_get_element(self.driver, By.CSS_SELECTOR, '.auth-header')
        return element.text

    def username_label_is_present(self):
        element = Utils.wait_presence_and_get_element(self.driver, By.CSS_SELECTOR, '.form-group label')
        return element.text

    def get_username_box(self):
        return Utils.wait_presence_and_get_element(self.driver, By.ID, 'username')

    def username_img_is_present(self):
        return Utils.wait_presence_and_get_element(self.driver, By.CSS_SELECTOR, '.form-group .pre-icon')

    def password_label_is_present(self):
        element = Utils.wait_presence_and_get_element(self.driver, By.CSS_SELECTOR, '.form-group:nth-child(2)')
        return element.text

    def get_password_box(self):
        return Utils.wait_presence_and_get_element(self.driver, By.ID, 'password')

    def password_img_is_present(self):
        return Utils.wait_presence_and_get_element(self.driver, By.CSS_SELECTOR, '.form-group:nth-child(2) .pre-icon')

    def get_login_button(self):
        return Utils.wait_clickable_and_get_element(self.driver, By.ID, 'log-in')

    def remember_me_button_is_clickable(self):
        return Utils.wait_clickable_and_get_element(self.driver, By.CSS_SELECTOR, '.form-check-input')

    def get_remember_me_label_text(self):
        return Utils.wait_presence_and_get_element(self.driver, By.CSS_SELECTOR, '.form-check-label')

    def count_social_media_imgs(self):
        elements = Utils.find_elements(self.driver, By.CSS_SELECTOR, '.buttons-w a')
        count = 0
        for x in elements:
            count = count + 1;
        return count

    def set_username(self, value):
        element = self.get_username_box()
        element.send_keys(value)

    def set_password(self, value):
        element = self.get_password_box()
        element.send_keys(value)

    def click_login_button(self):
        element = self.get_login_button()
        element.click()

    def get_warning_msg(self):
        element = Utils.wait_presence_and_get_element(self.driver, By.CSS_SELECTOR, '.alert-warning')
        return element.text

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()













