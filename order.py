from product import Product
from order_line import OrderLine


class Order:

    def __init__(self, order_id: str) -> None:
        #remove leading/trailing spaces and standardise the order ID
        order_id = order_id.strip().upper()

        #order ID cannot be empty
        if not order_id:
            raise ValueError("Order ID cannot be empty.")

        #store the order ID and its collection of order lines
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        #create the order line inside the order
        order_line = OrderLine(product, quantity)

        #store the order line as part of this order
        self.__order_lines.append(order_line)

    def remove_order_line(self, line_number: int) -> None:
        #line numbers start from 1
        if type(line_number) is not int:
            raise ValueError("Line number must be a whole number.")

        if line_number < 1 or line_number > len(self.__order_lines):
            raise ValueError("Order line not found.")

        #remove the order line managed by this order
        self.__order_lines.pop(line_number - 1)

    def calculate_total(self) -> float:
        #ask each order line to calculate its own subtotal
        return sum(
            (order_line.calculate_subtotal()
             for order_line in self.__order_lines),
            0.0
        )

    def display_information(self) -> None:
        #display the order and its order lines
        print(f"\nOrder ID: {self.__order_id}")
        print("-" * 72)

        if not self.__order_lines:
            print("Order is empty.")

        for line_number, order_line in enumerate(
            self.__order_lines,
            start=1
        ):
            print(f"Line {line_number}:")
            order_line.display_information()

        print("-" * 72)
        print(f"Order Total: ${self.calculate_total():.2f}")