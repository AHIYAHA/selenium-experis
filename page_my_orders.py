from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyOrders:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def orders(self):
        """מחזיר רשימה של שורות, כל שורה הזמנה"""
        return self.driver.find_element(By.ID, "myAccountContainer").find_elements(By.TAG_NAME, "tr")[1:]

    def order_number(self, i):
        """מחזיר את מספר ההזמנה, המופיע בתא הראשון בשורה"""
        num = self.orders()[i].find_elements(By.TAG_NAME, "td")[0]
        self.wait.until(EC.visibility_of(num))
        return num.text
