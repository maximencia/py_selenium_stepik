import math

from selenium import webdriver
import time


try:


    #     #Открыть страницу http://suninjuly.github.io/math.html.
    browser = webdriver.Chrome()
    # Тест успешно проходит на странице
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)
finally:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    # Считать значение для переменной x.
    # Посчитать математическую функцию от x (код для этого приведён ниже).
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    print(y)
    # Ввести ответ в текстовое поле.
    element = browser.find_element_by_id("""answer""")
    element.send_keys(y)
    # Отметить checkbox "I'm the robot".
    option2 = browser.find_element_by_css_selector("[for='robotCheckbox']")
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







# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
# Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера, но сложным для человека.
#
# Ваша программа должна выполнить следующие шаги:
#
# Открыть страницу http://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.
# Для этой задачи вам понадобится использовать атрибут .text для найденного элемента. Обратите внимание, что скобки здесь не нужны:
#
# x_element = browser.find_element_by_*(selector)
# x = x_element.text
# y = calc(x)
# Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. Например, text для данного элемента <div class="message">У вас новое сообщение.</div> вернёт строку: "У вас новое сообщение".
#
# Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Не забудьте добавить этот код в начало вашего скрипта:
#
# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже.