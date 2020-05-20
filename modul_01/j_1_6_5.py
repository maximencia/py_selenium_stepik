#
# Задание: поиск элемента по тексту в ссылке
# В этой задаче мы попробуем искать элементы по тексту ссылки, для этого воспользуемся методом
# find_element_by_link_text:
#
# link = browser.find_element_by_link_text(text)
# В качестве аргумента в метод передается такой текст, ссылку с которым мы хотим найти. Это тот самый текст, который
# содержится между открывающим и закрывающим тегом <a> вот тут </a>
#
# Допустим, на странице https://www.degreesymbol.net/ мы хотим найти ссылку с текстом "Degree symbol examples" и перейти
# по ней. Если хотим найти элемент по полному соответствию текста, то нам подойдет такой код:
#
# link = browser.find_element_by_link_text("» Degree symbol examples")
# link.click()
# А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код:
#
# link = browser.find_element_by_partial_link_text("examples")
# link.click()
# Обычно поиск по подстроке чуть более удобный и гибкий, но с ним надо быть вдвойне аккуратными и проверять, что наход
# ится нужный элемент.
#
# Задание
# На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:
#
# Добавьте в самый верх своего кода import math
# Добавьте команду в код, которая откроет страницу: http://suninjuly.github.io/find_link_text
# Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
# str(math.ceil(math.pow(math.pi, math.e)*10000))
# (можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже
# его использовать в вашем коде)
#
# Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
#
# Заполните скриптом форму так же как вы делали в предыдущем шаге урока
#
# После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание
# Важно! Поиск по тексту ссылки бывает очень удобным, так часто тексты меняются реже, чем атрибуты элементов. Но лучше
# избегать такого метода поиска. Например, если приложение имеет несколько языков интерфейса, ваши тесты будут проходить
# только с определенным языком интерфейса. Применяйте этот метод с осторожностью и помните про возможные ограничения.
#
# Читать больше:
#
# https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text
#

from selenium import webdriver
import time
import math

link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    print(link_text)

    link = browser.find_element_by_link_text(link_text)
    link.click()

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("firstname")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
