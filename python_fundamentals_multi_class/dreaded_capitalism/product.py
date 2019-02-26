class Product:
    def __init__(self, product_name, product_price, tax_rate):
        self.product_name = product_name
        self.product_price = product_price
        self.tax_rate = tax_rate

    def __eq__(self, other):
        return self.product_name == other.product_name

    def __str__(self):
        return "{} cost {}".format(self.product_name, self.product_price)
