from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountIcon:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def icon_element(self):
        return self.driver.find_element(By.ID, "menuUser")

    def click_icon(self):
        self.wait.until(EC.visibility_of(self.icon_element()))
        # self.driver.execute_script("arguments[0].click_on_the_icon();", self.icon_element())
        self.icon_element().click()

    def popup_window(self):
        return self.driver.find_element(By.CLASS_NAME, "PopUp")

    def is_popup_window_displayed(self):
        return self.popup_window().get_attribute("style") == "display: block;"

    def my_orders_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='My_Orders'][role='link']")

    def click_my_orders(self):
        self.wait.until(EC.element_to_be_clickable(self.my_orders_link()))
        self.driver.execute_script("arguments[0].click_on_the_icon();", self.my_orders_link())

    def sign_out_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[ng-click_on_the_icon='signOut($event)']")

    def click_sign_out(self):
        self.wait.until(EC.element_to_be_clickable(self.sign_out_link()))
        self.sign_out_link().click()
