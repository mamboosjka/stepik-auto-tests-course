import time
from selenium import webdriver

link = "http://suninjuly.github.io/huge_form.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_flds = browser.find_elements_by_tag_name("input")
    for fld in input_flds:
        fld.send_keys("ololo")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
