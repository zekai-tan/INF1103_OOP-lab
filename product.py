import math


class Product:
    def __init__(self, product_id, name, price, stock):
        product_id = product_id.strip().upper()
        name = name.strip()

        if not product_id or not name:
            raise ValueError("Product ID and name cannot be empty.")

        if not math.isfinite(price) or price < 0:
            raise ValueError("Price must be a finite, non-negative number.")

        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.update_stock(stock)

    def get_product_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        if type(quantity) is not int or quantity < 0:
            raise ValueError("Stock must be a non-negative whole number.")

        self.__stock = quantity

    def display_information(self):
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }