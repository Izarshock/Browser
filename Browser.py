from selenium import webdriver
import HtmlTestRunner
import unittest

driver = webdriver.Chrome()

driver.get("https://www.google.com")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reportes'))