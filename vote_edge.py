import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_edge_driver():
    """
    Функція створює і повертає об'єкт WebDriver для Microsoft Edge.
    Webdriver-manager сам підвантажує відповідний EdgeDriver.
    """
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    return driver

if __name__ == "__main__":
    driver = create_edge_driver()
    wait = WebDriverWait(driver, 10)  # Макс. час очікування елементів – 10 секунд

    # Тут приклад посилання на голосування (замініть на потрібне, якщо воно інше)
    website_url = "https://agroportal.ua/publishing/klub-agroeffektivnosti/vseukrajinskiy-konkurs-sila-agrozmin-onlayn-golosuvannya"

    # Локатори (XPATH)
    person_xpath = "//div[@aria-describedby='OperationDesc_73']"  # Наприклад, Шеховцов Євген
    choose_button_xpath = "//button[@class='btn btn-primary' and @data-test='choose-btn']"

    try:
        driver.get(website_url)

        # Очікуємо появи та клікабельності "кандидата"
        person_element = wait.until(EC.element_to_be_clickable((By.XPATH, person_xpath)))
        person_element.click()

        # Потім кнопка "Обрати"
        choose_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, choose_button_xpath)))
        choose_button_element.click()

        # Коротка пауза, щоб побачити результат
        time.sleep(2)
        print("Голос успішно віддано (Edge)!")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    finally:
        driver.quit()
