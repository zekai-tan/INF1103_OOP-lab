import math
from product import Product

class PhysicalProduct(Product):

    def __init__(self, product_id, name, price, stock, weight):
        #reuse the parent constructor for the common product attributes
        super().__init__(product_id, name, price, stock)

        #weight is finite and non-negative.
        if not math.isfinite(weight) or weight < 0:
            raise ValueError("Weight must be a finite and non-negative number.")

        #store the attribute specific to a physical product
        self.__weight = weight

    def display_information(self):
        #display information from the parent class
        super().display_information()

        #display additional physical product information
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
        #return the fulfilment information for a physical product
        return "This product requires physical shipping."