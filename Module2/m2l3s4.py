import time
import math
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.find_element_by_css_selector("button.btn").click()
    alert = browser.switch_to_alert()
    print(alert.text)
    alert.accept()
    x = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()

