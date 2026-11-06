import math
from product import Product
from shipping import CanBeShipped
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier
    ) -> None:
        #reuse the parent constructor for the common product attributes
        super().__init__(product_id, name, price, stock, supplier)

        #weight is finite and non-negative.
        if not math.isfinite(weight) or weight < 0:
            raise ValueError("Weight must be a finite and non-negative number.")

        #store the attribute specific to a physical product
        self.__weight: float = weight

    def display_information(self) -> None:
        #display information from the parent class
        super().display_information()

        #display additional physical product information
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self) -> str:
        #return the fulfilment information for a physical product
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        #calculate shipping using a chosen rate of 5.00 per kilogram
        return round(self.__weight * 5.00, 2)

    def to_dict(self) -> dict[str, str | float | int]:
        #reuse the parent method to get the common product attributes
        data = super().to_dict()

        #include the product type and its additional attribute
        data["type"] = "physical"
        data["weight"] = self.__weight

        return data