from product import Product

# Each shopping cart has a collection of products. It should also have the following functionality:

# 1 add an product to the cart
# 2 remove an product from the cart
# 3 add up the total cost of all products in the cart before tax
# 4 add up the total cost of all products in the cart after tax


class ShoppingCart:

    def __init__(self):
        self.cart = []

    def __str__(self):
        return "There are {} items".format(len(self.cart))

    def add_product(self, prod):
        self.cart.append(prod)

    def remove_product(self, prod):
        self.cart.remove(prod)


shopping_cart = ShoppingCart()
shopping_cart.add_product(Product('macbook', 1199, 0.13))
print(shopping_cart)
shopping_cart.remove_product(Product('macbook', 1199, 0.13))
# shopping_cart.add_product(Product('macbook', 1199, 0.13))
print(shopping_cart)
