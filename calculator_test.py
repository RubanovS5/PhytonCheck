from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
Chrome_driver = webdriver.Chrome()
@pytest.fixture(scope="module")
def driver():
    webdriver.Chrome()

def test_form():
    Chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay = Chrome_driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys("45")
    Chrome_driver.find_element(By.XPATH,"//span[text()='7']").click()               
    Chrome_driver.find_element(By.XPATH,"//span[text()='+']").click()
    Chrome_driver.find_element(By.XPATH,"//span[text()='8']").click()
    Chrome_driver.find_element(By.XPATH,"//span[text()='=']").click()

    result = WebDriverWait(Chrome_driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    result_text = Chrome_driver.find_element(By.CLASS_NAME, "screen").text
    assert result_text == "15"





