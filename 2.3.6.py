import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, ".trollface")
button.click()
new_win = new_window = browser.window_handles[1]
browser.switch_to.window(new_win)
x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
y = calc(x)
field = browser.find_element(By.CSS_SELECTOR, "input[type='text']")
field.send_keys(y)
btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
btn.click()