import itertools


class Product:
    """
        Product from our offer
        ...
        :param int self.id: unique product id
        :param str name: product name
        :param int price: product price
    """
    id_iter = itertools.count()

    def __init__(self, name, price):
        self.id = next(self.id_iter)
        self.name = name
        self.price = price

    def __str__(self):
        return f"id:{self.id} name:{self.name}"


class ShoppingCart:
    """
        Shopping Cart consisting of products from product class
        ...
        :param dict self.products: product id and name
        :param dict self.quantities: product id and quantity
        :param dict self.prices: product id and price
        :param float self.percentage_discount: percentage discount
    """
    def __init__(self):
        self.products = {}
        self.quantities = {}
        self.prices = {}
        self.percentage_discount = 0.30

    def add_product(self, product):
        """
        :param class product: instance of product class
        """
        if product.id in self.products:
            self.quantities[product.id] += 1
        else:
            self.products[product.id] = product.name
            self.quantities[product.id] = 1
            self.prices[product.id] = product.price

    def remove_product(self, product):
        """
        :param class product: instance of class product
        """
        if product.id in self.products:
            del self.products[product.id]
            del self.quantities[product.id]

    def change_product_quantity(self, product, new_quantity):
        """
        :param class product: instance of product class
        :param int new_quantity: new product quantity
        """
        if product.id in self.products:
            if new_quantity > 0:
                self.quantities[product.id] = new_quantity
            elif new_quantity == 0:
                self.remove_product(product)
            else:
                raise ValueError("Bad product quantity")

    def get_receipt(self):
        """
        :return: str receipt with all products and total amount to pay
        """
        receipt = ""
        total = 0
        for product in self.products:
            total_product = self.prices[product] * self.quantities[product]
            if self.quantities[product] > 2:
                discount = ((self.prices[product] * self.quantities[product]) * self.percentage_discount)
                total_product = total_product - discount
            total += total_product

            receipt += "\n" + self.products[product] + " " + "-" + " " + \
                       "amount:" + " " + str(self.quantities[product]) + "," + " " \
                       + "price:" + " " + str(self.prices[product]) + "zł" + "," + " " + "total:" + " " \
                       + str(total_product) + "zł"

        receipt += "\n" + "\n" + "Total:" + " " + str(total) + "zł"
        return receipt

    def __str__(self):
        return f"product names {self.products} product quantities:{self.quantities}"


if __name__ == '__main__':
    product_1 = Product("cup", 3)
    product_2 = Product("glasses", 4)
    product_3 = Product("cup", 5)
    product_4 = Product("computer", 1000)
    product_5 = Product("flowers", 10)
    first_list = ShoppingCart()
    second_list = ShoppingCart()
    first_list.add_product(product_1)
    first_list.add_product(product_1)
    first_list.add_product(product_2)
    first_list.add_product(product_2)
    first_list.add_product(product_2)
    first_list.add_product(product_3)
    first_list.change_product_quantity(product_1, 5)
    print(first_list.get_receipt())
    second_list.add_product(product_4)
    second_list.add_product(product_4)
    second_list.add_product(product_4)
    second_list.add_product(product_5)
    print(second_list.get_receipt())
