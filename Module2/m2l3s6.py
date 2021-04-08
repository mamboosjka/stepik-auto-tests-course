import time
import math
from selenium import webdriver

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    browser.get(link)
    submit_btn = browser.find_element_by_css_selector('button.btn')
    submit_btn.click()
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)
    x = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_css_selector('button.btn').click()
finally:
    time.sleep(10)
    browser.quit()