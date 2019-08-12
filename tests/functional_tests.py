import unittest
from selenium import webdriver


class FunctionalTest(unittest.TestCase): 

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        # self.driver.maximize_window()
        inst.driver.get("https://www.glenwoodspringsart.com/")

    def test_home_title(self):
        self.assertIn("The New Bridge Gallary", self.driver.title)

    # def test_logo(self):
        # elem = self.driver.find_element_by_class_name("navbar-brand")
        # self.assertIn("new_bridge_small.gif", elem)

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

if __name__ == "__main__":
    unittest.main()

