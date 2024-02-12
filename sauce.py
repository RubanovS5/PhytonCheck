from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


Chrome_driver = webdriver.Chrome()
Chrome_driver.maximize_window()
Chrome_driver.get("https://www.saucedemo.com/")

#Ввод логина и пароль
Chrome_driver.find_element(By.XPATH, "//input[@type='text']").send_keys("standard_user")
Chrome_driver.find_element(By.XPATH, "//input[@type='password']").send_keys("secret_sauce")
Chrome_driver.find_element(By.XPATH,"//input[@id='login-button']").click()

#Дабавление трех товаров в корзину
WebDriverWait(Chrome_driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@id = 'add-to-cart-sauce-labs-backpack']"))).click()
WebDriverWait(Chrome_driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@id = 'add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
WebDriverWait(Chrome_driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@id = 'add-to-cart-sauce-labs-onesie']"))).click()
Chrome_driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

Chrome_driver.find_element(By.XPATH, "//button[@id='checkout']").click()

#Заполнение личных данных
WebDriverWait(Chrome_driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'first-name']"))).send_keys("Александр")
WebDriverWait(Chrome_driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'last-name']"))).send_keys("Рубанов")
WebDriverWait(Chrome_driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'postal-code']"))).send_keys("195764")
Chrome_driver.find_element(By.XPATH, "//input[@type='submit']").click()

#Итоговая сумма
summa = WebDriverWait(Chrome_driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, "//div[@class='summary_info_label summary_total_label']"))).text
print(summa)
# Закрытие браузера
Chrome_driver.quit()

# Проверка итоговой суммы
total = 'Total: $58.29'
if total == summa:
    print("Итоговая сумма соответсвует ожидаемой")
else:
    print("Итоговая сумма не соответсвует ожидаемой")

