import math

from selenium import webdriver
import time

try:
    #     #Открыть страницу http://suninjuly.github.io/math.html.
    browser = webdriver.Chrome()
    # Тест успешно проходит на странице
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
finally:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    # Считать значение для переменной x.
    # Посчитать математическую функцию от x (код для этого приведён ниже).
    robots_radio = browser.find_element_by_id("treasure")
    x = robots_radio.get_attribute("valuex")

    y = calc(x)
    print(y)
    # Ввести ответ в текстовое поле.
    element = browser.find_element_by_id("""answer""")
    element.send_keys(y)
    # Отметить checkbox "I'm the robot".
    option2 = browser.find_element_by_id("robotCheckbox")
    option2.click()
    # Выбрать radiobutton "Robots rule!".
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    # Нажать на кнопку Submit.
    button = browser.find_element_by_xpath("""//button[@type="submit"][@class="btn btn-default"]""")
    button.click()

    time.sleep(15)
    # успеваем скопировать код за 30 секунд
    # уменьшим до 15 чтобы не ждать ошибки пол минуты
    # закрываем браузер после всех манипуляций
    browser.quit()
