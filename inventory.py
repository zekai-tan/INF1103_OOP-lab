from product import Product


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Inventory only accepts Product objects.")

        if self.search_product(product.get_product_id()) is not None:
            raise ValueError("A product with this ID already exists.")

        self.__products.append(product)

    def search_product(self, product_id):
        product_id = product_id.strip().upper()

        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        if not self.__products:
            print("\nInventory is empty.")
            return

        print("\nCurrent Inventory")
        print("-" * 72)

        for product in self.__products:
            product.display_information()

        print("-" * 72)

    def get_products(self):
        return self.__products.copy()