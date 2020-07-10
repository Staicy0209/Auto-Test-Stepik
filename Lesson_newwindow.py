from selenium import webdriver
import time
import math
from math import log, sin
link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
valuex = x_element.text
x = valuex
y = calc(x)
answer = browser.find_element_by_id("answer")
answer.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()