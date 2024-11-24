from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Payment:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def registration_button(self):
        return self.driver.find_element(By.ID, "registration_btn")

    def skip_shipping_details(self):
        """לוחץ על next בעמוד פרטי משלוח"""
        self.driver.find_element(By.ID, "next_btn").click()

    def choose_payment_method(self, i):
        radio = self.driver.find_elements(By.XPATH, "//*[@type='radio']")[i]
        if not radio.is_selected():
            radio.click()

    def order_number(self):
        """מחזיר את מספר ההזמנה המופיע בעמוד הסופי של הצלחת ביצוע הזמנה"""
        num = self.driver.find_element(By.ID, "orderNumberLabel")
        self.wait.until(EC.visibility_of(num))
        return num.text

    # safepay details

    def safepay_username(self):
        return self.driver.find_element(By.NAME, "safepay_username")

    def enter_safepay_username(self, username):
        self.safepay_username().send_keys(username)

    def safepay_password(self):
        return self.driver.find_element(By.NAME, "safepay_password")

    def enter_safepay_password(self, password):
        self.safepay_password().send_keys(password)

    def pay_safepay_button(self):
        return self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")

    def click_pay_safepay_button(self):
        self.wait.until(EC.element_to_be_clickable(self.pay_safepay_button()))
        self.pay_safepay_button().click()

    # credit details

    def credit_num_field(self):
        return self.driver.find_element(By.ID, "creditCard")

    def enter_creditcard_num(self, num):
        self.credit_num_field().send_keys(num)

    def CVV_field(self):
        return self.driver.find_element(By.NAME, "cvv_number")

    def enter_CVV_num(self, num):
        self.CVV_field().click()  # כי לא תמיד מכניס את הערכים
        self.CVV_field().send_keys(num)

    def month_expiration(self):
        return Select(self.driver.find_element(By.NAME, "mmListbox"))

    def year_expiration(self):
        return Select(self.driver.find_element(By.NAME, "YYYYListbox"))

    def change_month_expiration(self, month):
        self.month_expiration().select_by_visible_text(month)

    def change_year_expiration(self, year):
        self.year_expiration().select_by_visible_text(year)

    def cardholder_field(self):
        return self.driver.find_element(By.NAME, "cardholder_name")

    def enter_cardholder_name(self, num):
        self.cardholder_field().send_keys(num)

    def pay_credit_button(self):
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")

    # login

    def username_field_in_payment(self):
        return self.driver.find_element(By.NAME, "usernameInOrderPayment")

    def enter_username(self, username):
        self.username_field_in_payment().send_keys(username)

    def password_field_in_payment(self):
        return self.driver.find_element(By.NAME, "passwordInOrderPayment")

    def enter_password(self, password):
        self.password_field_in_payment().send_keys(password)

    def login_button(self):
        return self.driver.find_element(By.ID, "login_btn")



