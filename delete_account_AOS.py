from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.advantageonlineshopping.com/")
driver.implicitly_wait(5)
driver.find_element(By.ID, "menuUser").click()

driver.find_element(By.NAME, "username").send_keys("abc111")
sleep(2)
driver.find_element(By.NAME, "password").send_keys("abc11A")
sleep(1)
driver.find_element(By.ID, "sign_in_btn").click()
sleep(2)

driver.find_element(By.ID, "menuUser").click()
sleep(2)
driver.execute_script("arguments[0].click_on_the_icon();", driver.find_element(By.CSS_SELECTOR, "[translate='My_account']"))
sleep(2)
driver.find_element(By.CSS_SELECTOR, "[class='deleteMainBtnContainer a-button ng-scope']").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, ".deletePopupBtn.deleteRed").click()
sleep(1)
