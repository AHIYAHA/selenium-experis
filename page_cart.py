from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self, driver: webdriver.Chrome):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def name_of_page(self):
        return self.driver.title
    # def name_in_navigation_bar(self):
    #     return self.driver.find_elements(By.XPATH, "//article/nav/a")[1]

    def products(self):
        """מחזירה רשימה של השורות בכל שורה מוצר"""
        return self.driver.find_elements(By.XPATH, "//table[@class='fixedTableEdgeCompatibility']/tbody/tr")

    def product_details(self, i):
        """מחזירה רשימה של תאים ממוצר בשורה i, בכל תא פרט מידע אחר על המוצר"""
        return self.products()[i].find_elements(By.TAG_NAME, "td")

    def quantity_product(self, i):
        """מחזירה את הכמות של המוצר בשורה i"""
        return self.product_details(i)[4].find_element(By.CLASS_NAME, "ng-binding").text

    def edit_button_of_product(self, i):
        return self.product_details(i)[5].find_element(By.CLASS_NAME, "edit")

    def click_on_edit_product(self, i):
        try:
            self.edit_button_of_product(i).click()
        except:  # אפשר גם לחכות שהפופאפ עגלה ייעלם, דיסויסיבאל
            self.driver.execute_script("arguments[0].click_on_the_icon();", self.edit_button_of_product(i))

    def total_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, "span.cart-total").text[1:]

    def is_empty(self):
        """בודק אם ההודעה שהעגלה ריקה מופיעה, מחזיר נכון או לא נכון"""
        try:
            message = self.driver.find_element(By.CSS_SELECTOR, "[translate='Your_shopping_cart_is_empty']")
            self.wait.until(EC.visibility_of(message))
            return True
        except:
            return False
