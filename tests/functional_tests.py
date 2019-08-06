import unittest
from selenium import webdriver


class FunctionalTest(unittest.TestCase): 
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.driver.get("https://www.glenwoodspringsart.com/")
