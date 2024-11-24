from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def name_of_page(self):
        return self.driver.title
    # def row_sections(self):
    #     return self.driver.find_elements(By.CLASS_NAME, "rowSection")

    # def wait_connection(self):
    #     self.wait.until(EC.visibility_of(self.row_sections()[0]))

    def choose_category(self, ctg):
        """לוחץ על קטגוריה נתונה לפי ID"""
        self.driver.find_element(By.ID, ctg+"Img").click()

