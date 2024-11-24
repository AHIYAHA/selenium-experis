from selenium import webdriver
from selenium.webdriver.common.by import By


class Category:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def product(self, i):
        """מחזיר מוצר במקום הi בתוך רשימת המוצרים בקטגוריה לפי סדר הופעתם בעמוד"""
        self.driver.find_elements(By.CLASS_NAME, "imgProduct")[i].click()

    def name(self):
        return self.driver.title
    # def name(self):
    #     """מחזיר את שם העמוד"""
    #     return self.driver.find_element(By.CSS_SELECTOR, "article>h3").text
