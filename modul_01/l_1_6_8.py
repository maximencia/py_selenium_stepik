from selenium import webdriver
import time

# Задание: поиск элемента по XPath
# На этот раз воспользуемся возможностью искать элементы по XPath.
#
# На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3, при этом
# в нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Submit", и наша задача нажать
# в коде именно на неё.
#
# Ваши шаги:
#
# В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
# Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. XPath можете формулировать
# как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
# Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
# Запустите ваш код.
# Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код, который нужно отправить в качестве
# ответа на это задание.


try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_css_selector('[type="text"]')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_xpath("""//form/div/button[@class="btn"][ @type="submit"]""")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
