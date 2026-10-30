import math
from product import Product

class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size):
        #reuse the parent constructor for the common product attributes
        super().__init__(product_id, name, price, stock)

        #download size is finite and non-negative.
        if not math.isfinite(download_size) or download_size < 0:
            raise ValueError("Download size must be a finite and non-negative number.")

        #store the attribute specific to a digital product
        self.__download_size = download_size

    def display_information(self):
        #display information from the parent class
        super().display_information()

        #display additional digital product information
        print(f"Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self):
        #return the fulfilment information for a digital product
        return "This product is delivered digitally."

    def to_dict(self):
        #reuse the parent method to get the common product attributes
        data = super().to_dict()

        #include the product type and its additional attribute
        data["type"] = "digital"
        data["download_size"] = self.__download_size

        return data