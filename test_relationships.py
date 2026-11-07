from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory
from order import Order


def main() -> None:
    supplier = Supplier(
        "S001",
        "Tech Supplier",
        "supplier@example.com"
    )

    product = PhysicalProduct(
        "P001",
        "Laptop",
        1200.0,
        5,
        2.2,
        supplier
    )

    print("1. ASSOCIATION: Product -> Supplier")

    #product refers to the existing supplier object.
    assert product.get_supplier() is supplier

    product.get_supplier().display_information()

    print("PASS: Product references the same supplier object.")

    print("\n2. AGGREGATION: Inventory -> Product")

    inventory = Inventory()
    inventory.add_product(product)

    assert inventory.search_product("P001") is product

    inventory.remove_product("P001")

    assert inventory.search_product("P001") is None

    #product still exists outside the inventory.
    assert product.get_product_id() == "P001"
    product.display_information()

    print("PASS: Product still exists after removal from inventory.")

    print("\n3. COMPOSITION: Order -> OrderLine")

    order = Order("O001")

    #order creates its own line from a product and quantity.
    order.add_order_line(product, 2)

    assert order.calculate_total() == 2400.0

    order.display_information()

    print("PASS: Order creates and manages its order line.")

    #removing the order must not remove the referenced product.
    del order

    assert product.get_product_id() == "P001"

    print("PASS: Product still exists after the order is deleted.")

    print("\nAll relationship tests passed.")


if __name__ == "__main__":
    main()