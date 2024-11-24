from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopUpCart:
    def __init__(self, driver: webdriver.Chrome):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def click_on_the_icon(self):
        icon = self.driver.find_element(By.ID, "menuCart")
        self.wait.until(EC.element_to_be_clickable(icon))
        icon.click()

    def products_in_cart(self):
        """מחזיר רשימה של המוצרים שבעגלה"""
        return self.driver.find_elements(By.CSS_SELECTOR, "tr#product")

    def product_name(self, i):
        """מחזיר את שם המוצר לפי איך שהוא כתוב בעגלה בשורה הi"""
        return self.products_in_cart()[i].find_element(By.TAG_NAME, "h3").text

    def product_quantity(self, i):
        """מחזיר את כמות המוצר בשורה הi"""
        return self.products_in_cart()[i].find_element(By.TAG_NAME, "label").text[-1]

    def product_color(self, i):
        """מחזיר את צבע המוצר בשורה הi"""
        return self.products_in_cart()[i].find_element(By.TAG_NAME, "span").text

    def product_price(self, i):
        """מחזיר את מחיר המוצר בשורה הi ללא $"""
        return self.products_in_cart()[i].find_element(By.TAG_NAME, "p").text[1:]

    def remove_product(self, i):
        """לוחץ על איקס במוצר שבשורה הi"""
        self.products_in_cart()[i].find_element(By.CSS_SELECTOR, "[icon_element-x]").click()

    def num_of_items_total(self):
        """מחזיר מתוך האלמנט שכתוב בו מספר items בסוגריים, רק את המספר"""
        # מה עושים אם יש מוצר אחד, ואז כתוב אייטם ולא אייטמים?
        return self.driver.find_element(By.CSS_SELECTOR, "tfoot>tr>td>span>label").text[1:-7]

    def checkout(self):
        self.driver.find_element(By.ID, "checkOutPopUp").click()

