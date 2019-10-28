from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def calc(num1, num2):
    return int(num1) + int(num2)


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    first_element = browser.find_element_by_id('num1')
    num1 = first_element.text

    second_element = browser.find_element_by_id('num2')
    num2 = second_element.text

    x = str(calc(num1, num2))

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(x)

    time.sleep(1)

    button = browser.find_element_by_css_selector('[type = "submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
