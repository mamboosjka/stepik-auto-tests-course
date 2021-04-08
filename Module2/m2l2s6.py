import time
import math
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    x = int(browser.find_element_by_id("input_value").text)
    res = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(res))

    cb = browser.find_element_by_css_selector('input[type="checkbox"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', cb)
    cb.click()

    rb = browser.find_element_by_css_selector('input[type="radio"][name="ruler"][value="robots"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', rb)
    rb.click()

    submit_btn = browser.find_element_by_css_selector('button.btn[type="submit"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', submit_btn)
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()