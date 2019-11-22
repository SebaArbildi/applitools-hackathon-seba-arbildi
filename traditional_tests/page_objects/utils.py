from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Utils:
    @staticmethod
    def wait_presence_and_get_element(driver, selector, locator):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((selector, locator))
            )
        except:
            element = None
        return element

    @staticmethod
    def wait_clickable_and_get_element(driver, selector, locator):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((selector, locator))
            )
        except:
            element = None
        return element

    @staticmethod
    def find_elements(driver, selector, locator):
        try:
            elements = driver.find_elements(selector, locator)
        except:
            elements = None
        return elements

    @staticmethod
    def wait_for_visibility_get_element(driver, selector, locator):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of((selector, locator))
            )
        except:
            element = None
        return element

