import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Пакет webdriver_manager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def create_edge_driver():
    """
    Створюємо драйвер для Edge через webdriver-manager.
    Зверніть увагу: передаємо шлях у Service(...).
    """
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    return driver

if __name__ == "__main__":
    driver = create_edge_driver()
    wait = WebDriverWait(driver, 10)

    # Ваш URL голосування
    website_url = "https://agroportal.ua/publishing/klub-agroeffektivnosti/vseukrajinskiy-konkurs-sila-agrozmin-onlayn-golosuvannya"

    # XPATH-и, приклад
    person_xpath = "//div[@aria-describedby='OperationDesc_73']"
    choose_button_xpath = "//button[@class='btn btn-primary' and @data-test='choose-btn']"

    try:
        driver.get(website_url)

        # Очікуємо клікабельність "кандидата"
        person_element = wait.until(EC.element_to_be_clickable((By.XPATH, person_xpath)))
        person_element.click()

        # Те ж саме для кнопки "Обрати"
        choose_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, choose_button_xpath)))
        choose_button_element.click()

        time.sleep(2)
        print("Голос успішно віддано (Edge)!")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    finally:
        driver.quit()
