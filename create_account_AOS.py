from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.advantageonlineshopping.com/")
driver.implicitly_wait(5)
driver.find_element(By.ID, "menuUser").click()

sleep(4)
driver.find_element(By.CSS_SELECTOR, ".create-new-account.ng-scope").click()
sleep(2)
driver.find_element(By.NAME, "usernameRegisterPage").send_keys("abc112")
driver.find_element(By.NAME, "emailRegisterPage").send_keys("aaa@aaa.com")
driver.find_element(By.NAME, "passwordRegisterPage").send_keys("abc11A")
driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys("abc11A")
sleep(1)
driver.find_element(By.NAME, "i_agree").click()
sleep(1)
driver.find_element(By.ID, "register_btn").click()
