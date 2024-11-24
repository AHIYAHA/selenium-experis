from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def username_field(self):
        return self.driver.find_element(By.NAME, "username")

    def enter_username(self, username):
        self.username_field().send_keys(username)

    def password_field(self):
        return self.driver.find_element(By.NAME, "password")

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.password_field()))
        self.password_field().send_keys(password)

    def sign_in(self):
        return self.driver.find_element(By.ID, "sign_in_btn")

    def click_sign_in(self):
        """מחכה שהloader ייעלם ואז לוחץ על הכפתור"""
        loading = self.driver.find_element(By.CSS_SELECTOR, "login-modal>div>div>.loader")
        self.wait.until(EC.invisibility_of_element(loading))
        self.sign_in().click()
