import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Поиск фильмов на КиноПоиске")
@allure.story("Поиск по валидному символу")
def test_by_valid_symbol(chrome_browser):
    with allure.step("Открытие сайта КиноПоиск"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Ввод запроса '1+1'"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("1+1")
    with allure.step("Выбор фильма из предложенных"):
        chrome_browser.find_element(By.ID, "suggest-item-film-535341").click()
    with allure.step("Проверка названия фильма"):
        assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "1+1 (2011)"

@allure.feature("Поиск фильмов на КиноПоиске")
@allure.story("Поиск по невалидному символу")
def test_by_invalid_symbol(chrome_browser):
    with allure.step("Открытие сайта КиноПоиск"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Ввод невалидного запроса '%'"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("%")
    with allure.step("Проверка сообщения об отсутствии результатов"):
        assert chrome_browser.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"

@allure.feature("Поиск фильмов на КиноПоиске")
@allure.story("Поиск по русскому названию")
def test_search_by_russian_name(chrome_browser):
    with allure.step("Открытие сайта КиноПоиск"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Ввод запроса 'Зеленая миля'"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("Зеленая миля")
    with allure.step("Выбор фильма из предложенных"):
        chrome_browser.find_element(By.ID, "suggest-item-film-435").click()
    with allure.step("Проверка названия фильма"):
        assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Зеленая миля (1999)"

@allure.feature("Поиск фильмов на КиноПоиске")
@allure.story("Поиск по английскому названию")
def test_search_by_english_name(chrome_browser):
    with allure.step("Открытие сайта КиноПоиск"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Ввод запроса 'The Green Mile'"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("The Green Mile")
    with allure.step("Выбор фильма из предложенных"):
        chrome_browser.find_element(By.ID, "suggest-item-film-435").click()
    with allure.step("Проверка названия фильма"):
        assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "The Green Mile (1999)"
