from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Chrome_driver = webdriver.Chrome()
@pytest.fixture(scope="module")
def driver():
    webdriver.Chrome()

    
def test_form():
    Chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    Chrome_driver.find_element(By.XPATH, "//input[@name='first-name']").send_keys("Иван")
    Chrome_driver.find_element(By.XPATH, "//input[@name='last-name']").send_keys("Петров")
    Chrome_driver.find_element(By.XPATH, "//input[@name='address']").send_keys("Ленина, 55-3")
    Chrome_driver.find_element(By.XPATH, "//input[@name='zip-code']").send_keys("")
    Chrome_driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Москва")
    Chrome_driver.find_element(By.XPATH, "//input[@name='country']").send_keys("Россия")
    Chrome_driver.find_element(By.XPATH, "//input[@name='e-mail']").send_keys("test@skypro.com")
    Chrome_driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("+7985899998787")
    Chrome_driver.find_element(By.XPATH, "//input[@name='job-position']").send_keys("QA")
    Chrome_driver.find_element(By.XPATH, "//input[@name='company']").send_keys("SkyPro")
    Chrome_driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    WebDriverWait(Chrome_driver, 10, 0.1).until(EC.presence_of_element_located(By.XPATH, "//input[@id='zip-code']"))
    zip_color = zip.__getattribute__("color")
    print(zip_color)


    #expected_color = "rgb(245, 194, 199)"
   # if zip_color == expected_color:
 #       print("Красный цвет")
#else:
 ##      print("Не красный цвет")
  