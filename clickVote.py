import time
import sys

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def create_edge_driver():
    """Створює нову 'чисту' сесію Edge через webdriver-manager."""
    driver_path = EdgeChromiumDriverManager().install()
    service = EdgeService(driver_path)
    driver = webdriver.Edge(service=service)
    return driver

if __name__ == "__main__":
    print("Скрипт відкриває браузер на сторінці голосування.")
    print("Ви вручну обираєте людину (наприклад, Шеховцова Євгена) та тиснете 'Обрати'.")
    print("Після завершення голосування натисніть Enter у консолі, щоб закрити браузер і відкрити його знову.")
    print("Для виходу з цього циклу натисніть Ctrl + C.\n")

    website_url = (
        "https://agroportal.ua/publishing/klub-agroeffektivnosti/"
        "vseukrajinskiy-konkurs-sila-agrozmin-onlayn-golosuvannya"
    )

    iteration = 1
    while True:
        print(f"=== Ітерація №{iteration} ===")
        iteration += 1

        driver = create_edge_driver()
        driver.get(website_url)

        # Даємо час, щоб сторінка завантажилася
        time.sleep(2)

        # Тут користувач робить вибір вручну
        input("Натисніть Enter, коли ви завершили голосування у браузері...")

        # Закриваємо браузер і відкриємо знову на наступному колі
        driver.quit()

        # Коротка пауза, щоб було видно в консолі
        print("Браузер закрито. Зараз відкриємо нову чисту сесію...\n")
        time.sleep(1)
