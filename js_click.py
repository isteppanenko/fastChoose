import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def create_edge_driver():
    driver_path = EdgeChromiumDriverManager().install()
    service = EdgeService(driver_path)
    driver = webdriver.Edge(service=service)
    return driver

if __name__ == "__main__":
    driver = create_edge_driver()
    wait = WebDriverWait(driver, 15)

    website_url = "https://agroportal.ua/publishing/klub-agroeffektivnosti/vseukrajinskiy-konkurs-sila-agrozmin-onlayn-golosuvannya"

    # Елемент (для прикладу)
    person_xpath = "//div[@aria-describedby='OperationDesc_73']"
    choose_button_xpath = "//button[@class='btn btn-primary' and @data-test='choose-btn']"

    # Якщо існує cookie-банер (приклад), потрібно його закрити:
    cookie_banner_close_xpath = "//button[@id='cookie-close']"  # умовний XPATH, перевірте свій

    try:
        driver.get(website_url)

        # 1) Якщо є банер - перевіряємо, чи він з’являється:
        #    Якщо сайт реально має cookie-банер, шукаємо його XPATH,
        #    чекаємо і клікаємо "Прийняти" чи "Закрити". Якщо немає банера - цей крок пропускаємо.
        try:
            close_banner_btn = wait.until(EC.element_to_be_clickable((By.XPATH, cookie_banner_close_xpath)))
            close_banner_btn.click()
            print("Банер закрито.")
        except:
            print("Банера не знайдено / він не з’явився - пропускаємо.")

        # 2) Шукаємо "персону" - але замість to_be_clickable() перевіряємо visibility
        person_element = wait.until(EC.visibility_of_element_located((By.XPATH, person_xpath)))
        # Спробуємо через JS клік
        driver.execute_script("arguments[0].scrollIntoView(true);", person_element)
        driver.execute_script("arguments[0].click();", person_element)
        print("Клік по 'person_element' через JS виконано.")

        # 3) Аналогічно з кнопкою "Обрати"
        choose_button_element = wait.until(EC.visibility_of_element_located((By.XPATH, choose_button_xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", choose_button_element)
        driver.execute_script("arguments[0].click();", choose_button_element)
        print("Клік по кнопці 'Обрати' через JS виконано.")

        time.sleep(2)
        print("Голос успішно віддано (Edge)!")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    finally:
        driver.quit()
