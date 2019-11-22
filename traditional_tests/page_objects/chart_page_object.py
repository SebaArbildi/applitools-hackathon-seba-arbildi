import base64
import re

from PIL import Image, ImageChops
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from traditional_tests.page_objects.utils import Utils


class ChartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_show_next_year_button(self):
        button = Utils.wait_clickable_and_get_element(self.driver, By.ID, 'addDataset')
        button.click()

    def generate_chart_png(self, name):
        png_url = self.driver.execute_script('return document.getElementById("canvas").toDataURL("image/png")')
        str_base64 = re.search(r'base64,(.*)', png_url).group(1)
        str_decoded = base64.b64decode(str_base64)
        output_img = './tmp/{}.png'.format(name)
        fp = open(output_img, 'wb')
        fp.write(str_decoded)
        fp.close()

    def chart_2017_2018_is_valid(self, new_chart):
        are_equal = False
        actual = Image.open('./tmp/original_2017_2018.png')
        expected = Image.open('./tmp/{}.png'.format(new_chart))
        result_image = ImageChops.difference(actual, expected)

        if (ImageChops.difference(actual, expected).getbbox() is None):
            are_equal = True

        color_matrix = ([0] + ([255] * 255))
        result_image = result_image.convert('L')
        result_image = result_image.point(color_matrix)
        result_image.save('./tmp/result_2017_2018.png')  # Save the result image
        return are_equal

    def chart_2019_is_valid(self, new_chart):
        are_equal = False
        actual = Image.open('./tmp/original_2019.png')
        expected = Image.open('./tmp/{}.png'.format(new_chart))
        result_image = ImageChops.difference(actual, expected)

        if (ImageChops.difference(actual, expected).getbbox() is None):
            are_equal = True

        color_matrix = ([0] + ([255] * 255))
        result_image = result_image.convert('L')
        result_image = result_image.point(color_matrix)
        result_image.save('./tmp/result_2019.png')  # Save the result image
        return are_equal

