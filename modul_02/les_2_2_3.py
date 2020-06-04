import math

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    #Задание: работа с выпадающим списком
    # Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота,
    # чтобы он справился с новым заданием.
    #
    # Напишите код, который реализует следующий сценарий:
    #
    # Открыть страницу http://suninjuly.github.io/selects1.html
    # Посчитать сумму заданных чисел
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    # Нажать кнопку "Submit"
    # Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно
    # с числом. Отправьте полученное число в качестве ответа для этого задания.
    #
    #
    #
    # Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html. Ваш
    # код и для нее тоже ﻿должен пройти успешно.
    #
    # Подсказка: если вы получаете ошибку в духе "argument of type 'int' is not iterable", перепроверьте тип переменной,
    # которую вы передаете в функцию поиска. Нужно передать строку!
    #
    # Напишите текст
    browser = webdriver.Chrome()
    # Тест успешно проходит на странице
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)
finally:
    element = browser.find_element_by_id("""num1""")
    print(element.text)

    element2 = browser.find_element_by_id("""num2""")
    print(element2.text)
    sum=int(element.text)+int(element2.text)
    print(sum)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(sum))  # ищем элемент с текстом "Python"




    # Нажать на кнопку Submit.
    button = browser.find_element_by_xpath("""//button[@type="submit"][@class="btn btn-default"]""")
    button.click()

    time.sleep(15)
    # успеваем скопировать код за 30 секунд
    # уменьшим до 15 чтобы не ждать ошибки пол минуты
    # закрываем браузер после всех манипуляций
    browser.quit()
