import time
from selenium import webdriver

browser = webdriver.Chrome()
try:
    browser.execute_script("alert('Robots at work');")
finally:
    time.sleep(5)
    browser.quit()