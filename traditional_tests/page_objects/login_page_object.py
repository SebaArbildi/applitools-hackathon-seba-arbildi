
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def logo_big_img_is_present(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.logo-w img'))
        )

    def get_title(self, title):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.auth-header'))
        )
        return element.text

    def username_label_is_present(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.form-group label'))
        )
        return element.text

    def get_username_box(self):
         return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )

    def username_img_is_present(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.form-group .pre-icon'))
        )

    def password_label_is_present(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.form-group:nth-child(2)'))
        )
        return element.text

    def get_password_box(self):
         return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )

    def password_img_is_present(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.form-group:nth-child(2) .pre-icon'))
        )

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'log-in'))
        )

    def remember_me_button_is_clickeable(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.form-check-input'))
        )

    def get_remember_me_label_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.form-check-label'))
        )
        return element

    def count_social_media_imgs(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, '.buttons-w a')
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
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.alert-warning'))
        )
        return element.text

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()













