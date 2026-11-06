import math
from product import Product
from supplier import Supplier


class DigitalProduct(Product):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float,
        supplier: Supplier
    ) -> None:
        #reuse the parent constructor for the common product attributes
        super().__init__(product_id, name, price, stock, supplier)

        #download size is finite and non-negative.
        if not math.isfinite(download_size) or download_size < 0:
            raise ValueError("Download size must be a finite and non-negative number.")

        #store the attribute specific to a digital product
        self.__download_size: float = download_size

    def display_information(self) -> None:
        #display information from the parent class
        super().display_information()

        #display additional digital product information
        print(f"Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self) -> str:
        #return the fulfilment information for a digital product
        return "This product is delivered digitally."

    def to_dict(self) -> dict[str, str | float | int]:
        #reuse the parent method to get the common product attributes
        data = super().to_dict()

        #include the product type and its additional attribute
        data["type"] = "digital"
        data["download_size"] = self.__download_size

        return data