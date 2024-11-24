from unittest import TestCase
from selenium import webdriver
from automation_project.page_home import Home
from automation_project.page_category import Category
from automation_project.page_product import Product
from automation_project.popup_cart import PopUpCart
from automation_project.page_cart import Cart
from automation_project.account_icon import AccountIcon
from automation_project.page_register import Register
from automation_project.page_payment import Payment
from automation_project.popup_login import Login
from automation_project.page_my_orders import MyOrders
from automation_project.excel import Excel


def remove_str(my_str: str, sign: str):
    """static function to remove a sign from string, for the calculations in prices"""
    while sign in my_str:
        index = my_str.index(sign)
        my_str = my_str[:index] + my_str[index + 1:]
    return my_str


class TestShop(TestCase):
    def setUp(self):
        self.d = webdriver.Chrome()
        self.d.maximize_window()
        self.d.implicitly_wait(10)
        self.d.get("https://www.advantageonlineshopping.com/")

        self.home = Home(self.d)
        self.category = Category(self.d)
        self.product = Product(self.d)
        self.popup_cart = PopUpCart(self.d)
        self.cart = Cart(self.d)
        self.account_icon = AccountIcon(self.d)
        self.register = Register(self.d)
        self.login = Login(self.d)
        self.my_orders = MyOrders(self.d)
        self.payment = Payment(self.d)

        self.excel = Excel("data.xlsx")

    def tearDown(self):
        self.d.get("https://www.advantageonlineshopping.com/")
        self.d.close()

    def choose_product(self, category: str, product: int, quantity):
        self.home.choose_category(category)
        self.category.product(product)
        self.product.increase_quantity_to(quantity)
        self.product.add_to_cart()

    def test_1_popup_cart__total_quantity(self):
        """מוסיף שני מוצרים ובודק בעגלה שנפתחת למעלה מימין אם בסיכום כתוב מספר האייטמים הנכון"""
        column_of_test_in_excel = "C"
        self.excel.x(column_of_test_in_excel)

        # choose 2 product, according to data.xlsx
        num_of_products = 2
        for i in range(num_of_products):
            if i != 0:  # אפשר במקום לחזור אחורה ללחוץ על הלוגו
                self.d.back()
                self.d.back()
            self.choose_product(self.excel.category_of_product(i, column_of_test_in_excel),
                                self.excel.index_of_product(i, column_of_test_in_excel),
                                self.excel.quantity_of_product(i, column_of_test_in_excel))

        # checks if the total_price quantity is correct in the popup_window cart
        actual = int(self.popup_cart.num_of_items_total())
        excepted = 0
        for i in range(num_of_products):
            excepted += self.excel.quantity_of_product(i, column_of_test_in_excel)
        self.assertEqual(actual, excepted)
        self.excel.v(column_of_test_in_excel)

    def test_2_popup_cart__products_details(self):
        """מוסיף מוצרים, בודק שכל הפרטים מוצגים בחלונית העגלה: שם, צבע, כמות ומחיר. וגם מדפיס את כל הפרטים כפי שהם כתובים בדף המוצר"""
        column_of_test_in_excel = "D"
        self.excel.x(column_of_test_in_excel)

        # choose 3 product, according to data.xlsx
        num_of_products = 3
        names, quantities, colors, prices = [], [], [], []
        for i in range(num_of_products):
            if i != 0:
                self.d.back()
                self.d.back()
            self.home.choose_category(self.excel.category_of_product(i, column_of_test_in_excel))
            self.category.product(self.excel.index_of_product(i, column_of_test_in_excel))
            self.product.increase_quantity_to(self.excel.quantity_of_product(i, column_of_test_in_excel))
            names += [self.product.name()]
            quantities += [self.product.quantity()]
            colors += [self.product.color_selected()]
            prices += [self.product.price()]
            self.product.add_to_cart()

        # checks all the product details appearing, in the order of the cart - reverse
        for i in range(num_of_products-1, -1, -1):
            self.assertEqual(self.popup_cart.product_quantity(i), quantities[i])
            self.assertEqual(self.popup_cart.product_name(i), names[i])
            self.assertEqual(self.popup_cart.product_price(i), prices[i])
            self.assertEqual(self.popup_cart.product_color(i), colors[i])

        self.excel.v(column_of_test_in_excel)

    def test_3_popup_cart__remove_product(self):
        """בודק אם האיקס בחלונית העגלה מסיר את המוצר"""
        column_of_test_in_excel = "E"
        self.excel.x(column_of_test_in_excel)

        # choose 2 product, according to data.xlsx
        num_of_products = 2
        product_removed_name = ""
        for i in range(num_of_products):
            if i != 0:
                self.d.back()
                self.d.back()
            self.choose_product(self.excel.category_of_product(i, column_of_test_in_excel),
                                self.excel.index_of_product(i, column_of_test_in_excel),
                                self.excel.quantity_of_product(i, column_of_test_in_excel))
            product_removed_name = self.product.name()

        # remove first product
        self.popup_cart.remove_product(0)

        # check the product disappearing and the other appearing
        self.assertEqual(len(self.popup_cart.products_in_cart()), num_of_products - 1)
        self.assertEqual(self.popup_cart.product_name(0), product_removed_name)

        self.excel.v(column_of_test_in_excel)

    def test_4_popup_cart__open_cart_page_by_clicking(self):
        """בודקת שאחרי לחיצה על העגלה מגיעים לעמוד העגלה"""
        column_of_test_in_excel = "F"
        self.excel.x(column_of_test_in_excel)

        self.choose_product(self.excel.category_of_product(0, column_of_test_in_excel),
                            self.excel.index_of_product(0, column_of_test_in_excel),
                            self.excel.quantity_of_product(0, column_of_test_in_excel))
        self.popup_cart.click_on_the_icon()

        # checking
        self.assertEqual(self.cart.name_of_page(), "SHOPPING CART")
        self.excel.v(column_of_test_in_excel)

    def test_5_cart__total_price(self):
        column_of_test_in_excel = "G"
        self.excel.x(column_of_test_in_excel)

        # choose 3 product
        num_of_products, sum_prices = 3, 0
        for i in range(3):
            if i != 0:
                self.d.back()
                self.d.back()
            self.choose_product(self.excel.category_of_product(i, column_of_test_in_excel),
                                self.excel.index_of_product(i, column_of_test_in_excel),
                                self.excel.quantity_of_product(i, column_of_test_in_excel))

            # add the price to sum
            sum_prices += float(remove_str(self.product.price(), ",")) * int(self.product.quantity())

            # print product details
            print(f"name: {self.product.name()}, quantity: {self.product.quantity()}, price: {self.product.price()}")

        # go to cart page
        self.popup_cart.click_on_the_icon()

        # test result
        actual_total = float(remove_str(self.cart.total_price(), ","))
        self.assertEqual(sum_prices, actual_total)

        self.excel.v(column_of_test_in_excel)

    def test_6_cart__adding_quantity_to_products_in_the_cart(self):
        column_of_test_in_excel = "H"
        self.excel.x(column_of_test_in_excel)

        # choose 2 product
        num_of_products = 2
        for i in range(num_of_products):
            if i != 0:
                self.d.back()
                self.d.back()
            self.choose_product(self.excel.category_of_product(i, column_of_test_in_excel),
                                self.excel.index_of_product(i, column_of_test_in_excel),
                                self.excel.quantity_of_product(i, column_of_test_in_excel))

        # go to cart page
        self.popup_cart.click_on_the_icon()

        # changes, the order in the cart is reversed
        new_quantities = list()
        for i in range(num_of_products-1, -1, -1):
            new_quantities += [self.excel.quantity_of_product(i,column_of_test_in_excel) + 1]

        for i in range(num_of_products):
            self.cart.click_on_edit_product(i)
            self.product.increase_quantity_to(new_quantities[i])
            self.product.add_to_cart()
# defect! when changing the second item quantity - the quantity of the first is changing instead!
        # check if the changes appear
        for i in range(num_of_products):
            self.assertEqual(self.cart.quantity_product(i), new_quantities[i])

        self.excel.v(column_of_test_in_excel)

    def test_7_back_between_pages(self):
        column_of_test_in_excel = "I"
        self.excel.x(column_of_test_in_excel)

        self.choose_product(self.excel.category_of_product(0, column_of_test_in_excel),
                            self.excel.index_of_product(0, column_of_test_in_excel),
                            self.excel.quantity_of_product(0, column_of_test_in_excel))
        self.d.back()
        # check page
        self.assertEqual(self.category.name(), self.excel.category_of_product(0, column_of_test_in_excel).upper())

        self.d.back()
        # check page
        self.assertEqual(self.home.name_of_page(), "HOME")

        self.excel.v(column_of_test_in_excel)

    def test_8_payment_SafePay(self):
        column_of_test_in_excel = "J"
        self.excel.x(column_of_test_in_excel)

        self.choose_product(self.excel.category_of_product(0, column_of_test_in_excel),
                            self.excel.index_of_product(0, column_of_test_in_excel),
                            self.excel.quantity_of_product(0, column_of_test_in_excel))
        self.popup_cart.checkout()

        # page_account_registration.py
        self.payment.registration_button().click_on_the_icon()
        self.register.enter_username(self.excel.username(column_of_test_in_excel))
        self.register.enter_email(self.excel.email(column_of_test_in_excel))
        self.register.enter_password(self.excel.password(column_of_test_in_excel))
        self.register.select_i_agree()
        self.register.click_register()

        # payment in SafePay
        self.payment.skip_shipping_details()
        self.payment.choose_payment_method(0)
        self.payment.enter_safepay_username(self.excel.sp_username(column_of_test_in_excel))
        self.payment.enter_safepay_password(self.excel.sp_password(column_of_test_in_excel))
        self.payment.click_pay_safepay_button()

        # check order performing
        self.assertEqual(self.category.name(), "ORDER PAYMENT")
        order_num = self.payment.order_number()

        # check that the cart is empty
        self.popup_cart.click_on_the_icon()
        self.assertTrue(self.cart.is_empty())

        # check that the order appear in user's orders
        self.account_icon.click_icon()
        self.account_icon.click_my_orders()
        self.assertEqual(self.my_orders.order_number(-1), order_num)

        #  להוסיף קריאה לפונקציה שמוחקת את החשבון
        #
        # self.excel.v(column_of_test_in_excel)

    def test_9_payment_credit(self):
        column_of_test_in_excel = "K"
        self.excel.x(column_of_test_in_excel)

        self.choose_product(self.excel.category_of_product(0, column_of_test_in_excel),
                            self.excel.index_of_product(0, column_of_test_in_excel),
                            self.excel.quantity_of_product(0, column_of_test_in_excel))
        self.popup_cart.checkout()

        # login
        self.payment.enter_username(self.excel.username(column_of_test_in_excel))
        self.payment.enter_password(self.excel.password(column_of_test_in_excel))
        self.payment.login_button().click_on_the_icon()

        # payment in credit card
        self.payment.skip_shipping_details()
        self.payment.choose_payment_method(1)
        self.payment.enter_creditcard_num(self.excel.creditcard(column_of_test_in_excel))
        self.payment.enter_CVV_num(self.excel.cvv(column_of_test_in_excel))
        self.payment.enter_cardholder_name(self.excel.cardholder(column_of_test_in_excel))
        self.payment.pay_credit_button().click_on_the_icon()

        # check order performing
        self.assertEqual(self.category.name(), "ORDER PAYMENT")
        order_num = self.payment.order_number()

        # check that the cart is empty
        self.popup_cart.click_on_the_icon()
        self.assertTrue(self.cart.is_empty())

        # check that the order appear in user's orders
        self.account_icon.click_icon()
        self.account_icon.click_my_orders()
        self.assertEqual(self.my_orders.order_number(-1), order_num)

        self.excel.v(column_of_test_in_excel)

        # להוסיף קריאה לפונקציה שמוחקת את החשבון ויוצרת אותו מחדש

    def test_ten_connection(self):
        column_of_test_in_excel = "L"
        self.excel.x(column_of_test_in_excel)

        # login
        self.account_icon.click_icon()
        self.login.enter_username(self.excel.username(column_of_test_in_excel))
        self.login.enter_password(self.excel.password(column_of_test_in_excel))
        self.login.click_sign_in()
        # self.home.wait_connection()

        # check connection
        self.account_icon.click_icon()
        self.assertFalse(self.account_icon.is_popup_window_displayed())

        # logout
        self.account_icon.click_icon()
        self.account_icon.click_sign_out()
        # self.home.wait_connection()

        # check disconnection
        self.account_icon.click_icon()
        self.assertTrue(self.account_icon.is_popup_window_displayed())

        self.excel.v(column_of_test_in_excel)
