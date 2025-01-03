import time
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Якщо хочете використовувати Chrome, закоментуйте рядки з Edge
# та раскоментуйте наведені нижче імпорти:
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options as ChromeOptions

from webdriver_manager.microsoft import EdgeChromiumDriverManager


def create_edge_driver():
    """
    Створює і повертає WebDriver для Edge через webdriver-manager.
    Кожне створення драйвера = "чиста" сесія, без Cookies та історії.
    """
    driver_path = EdgeChromiumDriverManager().install()
    service = EdgeService(driver_path)
    driver = webdriver.Edge(service=service)
    return driver


def vote_for_shehovtsov():
    """
    Заходить на сторінку голосування, обирає Євгена Шеховцова,
    тисне "Обрати", виводить повідомлення.
    """
    # URL сторінки голосування
    website_url = (
        "https://agroportal.ua/publishing/klub-agroeffektivnosti/"
        "vseukrajinskiy-konkurs-sila-agrozmin-onlayn-golosuvannya"
    )

    # XPATH-локатори для Євгена Шеховцова та кнопки "Обрати"
    person_xpath = "//div[@aria-describedby='OperationDesc_73']"
    choose_button_xpath = (
        "//button[@class='btn btn-primary' and @data-test='choose-btn']"
    )

    driver = create_edge_driver()
    wait = WebDriverWait(driver, 10)  # до 10 с. очікування
    try:
        driver.get(website_url)

        # Клікаємо на "Євгена Шеховцова"
        person_element = wait.until(EC.element_to_be_clickable((By.XPATH, person_xpath)))
        person_element.click()

        # Клікаємо "Обрати"
        choose_button_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, choose_button_xpath))
        )
        choose_button_element.click()

        # Невелика пауза, щоб сайт зафіксував голос
        time.sleep(2)
        print("Голос віддано за Шеховцова Євгена!")
    except Exception as e:
        print(f"Помилка під час голосування: {e}")
    finally:
        driver.quit()  # Закриваємо браузер (очищаємо сесію)


if __name__ == "__main__":
    print("Починаємо нескінченне голосування...")
    iteration = 1
    try:
        while True:
            print(f"\n=== Ітерація #{iteration} ===")
            iteration += 1

            vote_for_shehovtsov()

            # Ви можете додати додаткову затримку між голосуваннями,
            # аби не "бомбардувати" сайт занадто швидко.
            # Наприклад, почекати 10 секунд:
            time.sleep(10)

    except KeyboardInterrupt:
        print("\nСкрипт зупинено користувачем. Завершення...")
        sys.exit(0)
