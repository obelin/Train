import unittest2 as unittest
from selenium import webdriver
import time

class Test1(unittest.TestCase):
    """ the first test
    """

    def __init__(self, *args, **kwargs):
        super(Test1, self).__init__(*args, **kwargs)
        self.driver = None

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_google(self):
        self.driver.get("http://google.com")

    def test_yandex(self):
        self.driver.get("http://yandex.com")

    def tearDown(self):
        time.sleep(3)

        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
