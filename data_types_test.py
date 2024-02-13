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

    assert Chrome_driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert Chrome_driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert Chrome_driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert Chrome_driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color") == "rgba(248, 215, 218, 1)"
    assert Chrome_driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert Chrome_driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert Chrome_driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert Chrome_driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert Chrome_driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert Chrome_driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
  

  