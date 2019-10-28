from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys('Bohdan')

    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys('Ipatov')

    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys('abc@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    button1 = browser.find_element_by_id('file')
    button1.send_keys(file_path)

    button2 = browser.find_element_by_css_selector('[type = "submit"]')
    button2.click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
