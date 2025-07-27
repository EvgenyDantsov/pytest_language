import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_see_add_to_basket_button(browser):
    # Открываем страницу товара
    browser.get(link)
    time.sleep(10)
    # Проверяем наличие кнопки добавления в корзину с явным ожиданием
    basket_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")),
        message="Кнопка добавления в корзину не найдена"
    )

    # Проверяем что кнопка существует (assert)
    assert basket_button, "Кнопка добавления в корзину должна присутствовать на странице"
