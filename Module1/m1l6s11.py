import time
from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    f_name = browser.find_element_by_css_selector('input.first[placeholder="Input your first name"]')
    f_name.send_keys("lol")

    l_name = browser.find_element_by_css_selector('input.second[placeholder="Input your last name"]')
    l_name.send_keys("oloa")

    email = browser.find_element_by_css_selector('input.third[placeholder="Input your email"]')
    email.send_keys("eml@gmail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(3)
    browser.quit()