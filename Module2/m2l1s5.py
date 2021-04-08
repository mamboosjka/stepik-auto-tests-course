import time
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element_by_id("input_value")
    x = int(x_el.text)
    fn_res = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(fn_res)

    cb = browser.find_element_by_css_selector('input[type="checkbox"]')
    cb.click()

    rb = browser.find_element_by_css_selector('input[type="radio"][name="ruler"][value="robots"]')
    rb.click()

    submit_btn = browser.find_element_by_css_selector('button.btn[type="submit"]')
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()


