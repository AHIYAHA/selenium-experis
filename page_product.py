from selenium import webdriver
from selenium.webdriver.common.by import By


class Product:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h1").text

    def quantity(self):
        return self.driver.find_element(By.NAME, "quantity").get_attribute("value")

    def price(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h2").text[1:]

    def color_selected(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#rabbit.colorSelected").get_attribute("title")

    def increase_quantity_to(self, num):
        """מגדיל את הכמות עד למספר הנתון. לא מסוגל להקטין כמות"""
        while num != int(self.quantity()):
            self.driver.find_element(By.CLASS_NAME, "plus").click()

    def add_to_cart(self):
        self.driver.find_element(By.NAME, "save_to_cart").click()
