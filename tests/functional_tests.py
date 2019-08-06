import unittest
from selenium import webdriver


class FunctionalTest(unittest.TestCase): 

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.driver.get("https://www.glenwoodspringsart.com/")

    def test_home_title(self):
        self.assertIn("The New Bridge Gallary", self.driver.title)

    # def test_logo(self):
        # elem = self.driver.find_element_by_class_name("navbar-brand")
        # self.assertIn("new_bridge_small.gif", elem)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

