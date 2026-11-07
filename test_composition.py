from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


def main() -> None:
    #create the supplier and products independently of the orders
    supplier = Supplier(
        "S001",
        "Tech Supplier",
        "supplier@example.com"
    )

    physical_product = PhysicalProduct(
        "TEST001",
        "Test Laptop",
        1200.0,
        5,
        2.2,
        supplier
    )

    digital_product = DigitalProduct(
        "TEST002",
        "Test Ebook",
        10.0,
        20,
        5.0,
        supplier
    )

    #create the first order and let it create its own order lines
    order_a = Order("O001")
    order_a.add_order_line(physical_product, 2)
    order_a.add_order_line(digital_product, 3)

    assert order_a.calculate_total() == 2430.0
    order_a.display_information()

    #reuse the same product in a different order
    order_b = Order("O002")
    order_b.add_order_line(physical_product, 1)

    assert order_b.calculate_total() == 1200.0
    order_b.display_information()

    #remove the physical product line through its owning order
    order_a.remove_order_line(1)

    assert order_a.calculate_total() == 30.0

    #the other order is unaffected
    assert order_b.calculate_total() == 1200.0

    #the product still exists independently
    assert physical_product.get_price() == 1200.0
    physical_product.display_information()

    #an empty order should have a total of zero
    empty_order = Order("O003")
    assert empty_order.calculate_total() == 0.0

    #invalid quantities should be rejected without adding a line
    try:
        empty_order.add_order_line(physical_product, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Zero quantity should be rejected.")

    assert empty_order.calculate_total() == 0.0

    print("\nAll composition tests passed.")


if __name__ == "__main__":
    main()