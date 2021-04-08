import time
import os
from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    f_name = browser.find_element_by_name("firstname")
    l_name = browser.find_element_by_name("lastname")
    email = browser.find_element_by_name("email")
    in_file = browser.find_element_by_css_selector('input[type="file"]')

    f_name.send_keys('ololo')
    l_name.send_keys('ololo')
    email.send_keys('ololo')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.abspath(os.path.join(current_dir, "file.txt"))
    #in_file.click()
    in_file.send_keys(file_path)

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()

