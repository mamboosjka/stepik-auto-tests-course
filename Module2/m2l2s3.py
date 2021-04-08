import time
import math
from selenium import webdriver
#import for second way
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    n1 = int(browser.find_element_by_id("num1").text)
    n2 = int(browser.find_element_by_id("num2").text)
    res = n1 + n2
    #first way
    # res_lst = browser.find_element_by_css_selector('select#dropdown')
    # res_lst.click()
    # res_row =browser.find_element_by_css_selector(f'select#dropdown>option[value="{str(res)}"]')
    # res_row.click()

    #second way
    res_lst = Select(browser.find_element_by_css_selector('select#dropdown'))
    res_lst.select_by_value(str(res))


    submit_btn = browser.find_element_by_css_selector('button.btn[type="submit"]')
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()
