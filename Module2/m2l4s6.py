import time
from selenium import webdriver

link = 'http://suninjuly.github.io/cats.html'

browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element_by_id("button")
finally:
    time.sleep(10)
    browser.quit()