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
    Chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay = Chrome_driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys("45")
    Chrome_driver.find_element(By.XPATH,"//span[text()='7']").click()               
    Chrome_driver.find_element(By.XPATH,"//span[text()='+']").click()
    Chrome_driver.find_element(By.XPATH,"//span[text()='8']").click()
    Chrome_driver.find_element(By.XPATH,"//span[text()='=']").click()
    res = Chrome_driver.find_element(By.XPATH,"//div[@class='screen']")
    otvet = WebDriverWait(Chrome_driver,45, 0.1).until(EC.presence_of_element_located(res))
    for element in otvet:
        print(element.text)
    Chrome_driver.quit()
    





