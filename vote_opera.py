import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Використання ChromeOptions для Opera

def create_opera_driver():
    options = Options()
    # Додаємо шлях до OperaDriver
    driver_path = r"C:\Users\istep\Downloads\operadriver_win64\operadriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, options=options)  # Використовуємо ChromeDriver для Opera
    return driver

if __name__ == "__main__":
    driver = create_opera_driver()

    # URL сторінки голосування
    website_url = "https://agroportal.ua/publishing/klub-agroeffektivnosti/vseukrajinskiy-konkurs-sila-agrozmin-onlayn-golosuvannya"

    # Локатори
    person_xpath = "//div[@aria-describedby='OperationDesc_73']"  # Вибір Шеховцова Євгена
    choose_button_xpath = "//button[@class='btn btn-primary' and @data-test='choose-btn']"  # Кнопка "Обрати"

    try:
        # Перехід на сайт
        driver.get(website_url)
        time.sleep(5)

        # Вибір Шеховцова Євгена
        person_element = driver.find_element(By.XPATH, person_xpath)
        person_element.click()
        time.sleep(2)

        # Натискання кнопки "Обрати"
        choose_button_element = driver.find_element(By.XPATH, choose_button_xpath)
        choose_button_element.click()
        time.sleep(3)

        print("Голос за Шеховцова Євгена успішно віддано!")

    except Exception as e:
        print(f"Сталася помилка: {e}")

    finally:
        driver.quit()
