import math
from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier
    ) -> None:
        product_id = product_id.strip().upper()
        name = name.strip()

        if not product_id or not name:
            raise ValueError("Product ID and name cannot be empty.")

        if not math.isfinite(price) or price < 0:
            raise ValueError("Price must be a finite and non-negative number.")

        #check that the supplier is a Supplier object
        if not isinstance(supplier, Supplier):
            raise TypeError("Supplier must be a Supplier object.")

        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price

        #store a reference to the independently created supplier
        self.__supplier: Supplier = supplier

        self.update_stock(stock)

    def get_product_id(self) -> str:
        return self.__product_id

    def get_price(self) -> float:
        #return the price without directly exposing the private attribute
        return self.__price

    def get_supplier(self) -> Supplier:
        #return the associated supplier object
        return self.__supplier

    def update_stock(self, quantity: int) -> None:
        if type(quantity) is not int or quantity < 0:
            raise ValueError("Stock must be a non-negative whole number.")

        self.__stock: int = quantity

    def display_information(self) -> None:
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

        #display information through the associated supplier object
        self.__supplier.display_information()

    def to_dict(self) -> dict[str, str | float | int]:
        #convert the common product attributes into a dictionary
        data: dict[str, str | float | int] = {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

        #include information from the associated supplier
        data.update(self.__supplier.to_dict())

        return data

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        #require each concrete subclass to implement this method.
        pass