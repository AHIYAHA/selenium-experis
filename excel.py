from openpyxl import load_workbook


class Excel:
    def __init__(self, address):
        self.address = address
        self.workbook = load_workbook(address)
        self.sheet = self.workbook.active

    def v(self, cell):
        self.sheet[cell+"19"] = "V"
        self.workbook.save(self.address)

    def x(self, cell):
        self.sheet[cell+"19"] = "X"

    def category_of_product(self, i, test_c):
        return self.sheet[f"{test_c}{2 + i * 3}"].value

    def index_of_product(self, i, test_c):
        return self.sheet[f"{test_c}{3 + i * 3}"].value

    def quantity_of_product(self, i, test_c):
        return self.sheet[f"{test_c}{4 + i * 3}"].value

    def username(self, test_c):
        return self.sheet[f"{test_c}11"].value

    def email(self, test_c):
        return self.sheet[f"{test_c}12"].value

    def password(self, test_c):
        return self.sheet[f"{test_c}13"].value

    def sp_username(self, test_c):
        return self.sheet[f"{test_c}14"].value

    def sp_password(self, test_c):
        return self.sheet[f"{test_c}15"].value

    def creditcard(self, test_c):
        return self.sheet[f"{test_c}16"].value

    def cvv(self, test_c):
        return self.sheet[f"{test_c}17"].value

    def cardholder(self, test_c):
        return self.sheet[f"{test_c}18"].value



