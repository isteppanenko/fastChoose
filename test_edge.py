import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Важливо: в Selenium-коді використовуємо об'єкт Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def create_edge_driver():
    """
    Функція створює та повертає об'єкт WebDriver для Microsoft Edge,
    використовуючи webdriver-manager і правильну передачу Service.
    """
    # 1. Менеджер завантажує / оновлює msedgedriver.exe під вашу версію Edge
    driver_path = EdgeChromiumDriverManager().install()
    # 2. "Загортаємо" шлях у об’єкт EdgeService
    service = EdgeService(driver_path)
    # 3. Створюємо WebDriver
    driver = webdriver.Edge(service=service)
    return driver

if __name__ == "__main__":
    driver = create_edge_driver()
    wait = WebDriverWait(driver, 10)

    try:
        # Відкриваємо Google
        driver.get("https://www.google.com")
        
        # Шукаємо поле пошуку (By.NAME, "q") і вводимо текст
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("Selenium Edge test")
        search_box.submit()

        time.sleep(3)
        print("Пошук у Google виконано успішно (Edge).")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    finally:
        driver.quit()
