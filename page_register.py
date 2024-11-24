from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Register:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def username_field(self):
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def enter_username(self, name):
        self.username_field().send_keys(name)

    def email_field(self):
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def enter_email(self, email):
        self.email_field().send_keys(email)

    def password_field(self):
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def confirm_password_field(self):
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def enter_password(self, password):
        self.password_field().send_keys(password)
        self.confirm_password_field().send_keys(password)

    def select_i_agree(self):
        """לא תמיד מצליח ללחוץ על המשבצת, לכן יש כאן וידוא"""
        radio = self.driver.find_element(By.NAME, "i_agree")
        while not radio.is_selected():
            self.wait.until(EC.element_to_be_clickable(radio))
            radio.click()

    def register_button(self):
        return self.driver.find_element(By.ID, "register_btn")

    def click_register(self):
        self.wait.until(EC.element_to_be_clickable(self.register_button()))
        self.register_button().click()

