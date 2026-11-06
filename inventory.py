from product import Product


class Inventory:

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Inventory only accepts Product objects.")

        if self.search_product(product.get_product_id()) is not None:
            raise ValueError("A product with this ID already exists.")

        self.__products.append(product)

    def search_product(self, product_id: str) -> Product | None:
        product_id = product_id.strip().upper()

        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def find_product(self, product_id: str) -> Product | None:
        #reuse the existing search method to find a product
        return self.search_product(product_id)

    def remove_product(self, product_id: str) -> Product | None:
        #find the product before removing its reference from the inventory
        product = self.find_product(product_id)

        if product is None:
            return None

        #remove the reference without destroying the product object
        self.__products.remove(product)

        return product

    def display_all(self) -> None:
        if not self.__products:
            print("\nInventory is empty.")
            return

        print("\nCurrent Inventory")
        print("-" * 72)

        for product in self.__products:
            product.display_information()

        print("-" * 72)

    def get_products(self) -> list[Product]:
        return self.__products.copy()