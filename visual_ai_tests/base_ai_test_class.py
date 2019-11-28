import os
import unittest

from applitools.common import BatchInfo
from applitools.selenium import Eyes
from selenium import webdriver


class BaseTestClass(unittest.TestCase):

    _batch = BatchInfo('Hackathon ')
    _url = 'https://demo.applitools.com/hackathonV2.html'

    def init(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.eyes = Eyes()
        self.eyes.api_key = os.environ['APPLITOOLS_API_KEY']
        self.eyes.batch = self._batch
        self.driver.get(self._url)
