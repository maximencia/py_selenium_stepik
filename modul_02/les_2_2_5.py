import math

from selenium import webdriver
import time,math
from selenium.webdriver.support.ui import Select

try:
    #ЗЗадание на execute_script
# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который
    # дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:
#
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с
    # числом. Отправьте полученное число в качестве ответа для этого задания.
#
# Для этой задачи вам понадобится использовать метод execute_script, чтобы сделать прокрутку в область видимости элем
    # ентов, перекрытых футером.
    browser = webdriver.Chrome()
    # Тест успешно проходит на странице
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
finally:
    print("What is ln(abs(12 * sin(x))), where")
    element = browser.find_element_by_id("""input_value""")
    print(element.text)
    x = math.log(abs(12 * math.sin(int(element.text))))
    print(x)
    #answer

    element = browser.find_element_by_id("""answer""")
    element.send_keys(str(x))


    #robotCheckbox
    # Отметить checkbox "I'm the robot".
    option2 = browser.find_element_by_id("robotCheckbox")
    option2.click()

    #нужно просколить до кнопки чтобы радиобатон тоже стал виден
    button = button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Выбрать radiobutton "Robots rule!".
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    button.click()


    time.sleep(15)
    # успеваем скопировать код за 30 секунд
    # уменьшим до 15 чтобы не ждать ошибки пол минуты
    # закрываем браузер после всех манипуляций
    browser.quit()
