from selenium import webdriver
import time

# Чтобы не дублировать код для проверки первого случая раскоментируем строку 9, а для второго 12.
# правильно делать 2 различных тестовых скрипта так как страницы разные

try:
    browser = webdriver.Chrome()
    # Тест успешно проходит на странице
    link = "http://suninjuly.github.io/registration1.html"

    # Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
    #link="http://suninjuly.github.io/registration2.html"
    browser.get(link)

    # 1
    element = browser.find_element_by_xpath(
        """//form/div[@class='first_block']/div[@class='form-group first_class']/input""")
    element.send_keys("Мой ответ")
    # 2
    element = browser.find_element_by_xpath(
        """//form/div[@class='first_block']/div[@class='form-group second_class']/input""")
    element.send_keys("Мой ответ")
    # 3
    element = browser.find_element_by_xpath(
        """//form/div[@class='first_block']/div[@class='form-group third_class']/input""")
    element.send_keys("Мой ответ")

    # 4
    element = browser.find_element_by_xpath(
        """//form/div[@class='second_block']/div[@class='form-group first_class']/input""")
    element.send_keys("Мой ответ")

    # 5
    element = browser.find_element_by_xpath(
        """//form/div[@class='second_block']/div[@class='form-group second_class']/input""")
    element.send_keys("Мой ответ")

    button = browser.find_element_by_xpath("""//button[@type="submit"][@class="btn btn-default"]""")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    # уменьшим до 15 чтобы не ждать ошибки пол минуты
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()



# Задание: уникальность селекторов
# Это задание с так называемым пир-ревью: правильность вашего решения будут проверять другие учащиеся. Также и вам пред
# стоит проверить чужой код. Ознакомившись с разными способами решения одной и той же задачи, вы сможете лучше понять
# изучаемую тему.
#
# У нас уже есть простой тест из предыдущего шага, который проверяет возможность зарегистрироваться на сайте. Однако
# разработчики решили немного поменять верстку страницы, чтобы она выглядела более современной. Обновленная страница
# доступна по другой ссылке. К сожалению, в процессе изменений они случайно внесли баг в форму регистрации.
#
# Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку. Если ваш тест упал
# с ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы и смогли обнаружить баг, который
# создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо. Пугаться не стоит, здесь ошибка в приложении
# которое вы тестируете, а не в вашем тесте.
#
# Если же ваш тест прошел успешно, то это означает, что тест пропустил серьезный баг. В этом случае попробуйте поменять
# селекторы, сделав их уникальными. После изменения убедитесь, что ваш тест исправно проходит в старой версии страницы.
#
# Чтобы получить максимальное количество баллов, прежде чем отправлять решение на рецензию, самостоятельно убедитесь в
# том что:
#
# Тест успешно проходит на странице http://suninjuly.github.io/registration1.html﻿
#
# Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
#
# Используемые селекторы должны быть уникальны
#
# Будьте внимательны, ведь на рецензирование работу можно отправить только один раз!
#
# Прикрепите файл с тестом к этому заданию, а затем отправьте его на рецензирование. Убедитесь что расширение файла .py
# а не .txt, иначе велика вероятность, что ваше решение не запустится у других. Убедитесь, что в вашем коде не указаны
# пути до хромдрайвера, иначе ваш код не запустится у других студентов. Если вы используете Firefox или что-то, что мы
# не проходили в курсе, добавьте комментарии о том, как запустить такой код. Помните, что ваш код будут проверять, в том
# числе, новички.
#
# Не забудьте посмотреть и отрецензировать работы других учащихся, только после этого вы получите баллы за данное
# задание.
#
# Кстати! Не удаляйте код после прохождения задания, он нам пригодится в будущих модулях.



# не забываем оставить пустую строку в конце файла
