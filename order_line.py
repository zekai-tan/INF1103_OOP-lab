from product import Product


class OrderLine:

    def __init__(self, product: Product, quantity: int) -> None:
        #check that the product is a Product object
        if not isinstance(product, Product):
            raise TypeError("Order line must refer to a Product object.")

        #quantity must be a positive whole number
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("Quantity must be a positive whole number.")

        #store the product reference and the quantity ordered
        self.__product: Product = product
        self.__quantity: int = quantity

    def calculate_subtotal(self) -> float:
        #calculate the subtotal using the product price and quantity
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        #display the product ID, quantity and subtotal
        print(
            f"Product ID: {self.__product.get_product_id()} | "
            f"Quantity: {self.__quantity} | "
            f"Subtotal: ${self.calculate_subtotal():.2f}"
        )