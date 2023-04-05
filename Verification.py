from selenium import webdriver
import unittest

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
    
    def test_page_title(self):
        self.assertEqual(self.driver.title, "Google")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
