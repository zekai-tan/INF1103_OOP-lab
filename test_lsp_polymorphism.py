from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from inventory import Inventory

def show_product_details(product: Product) -> None:
    #use the same function for any Product subclass
    product.display_information()
    print(product.get_fulfilment_info())

def test_stock_behaviour(product: Product) -> None:
    #both product types must support replacing the current stock
    for quantity in (0, 10, 3):
        result = product.update_stock(quantity)

        assert result is None
        assert product.to_dict()["stock"] == quantity

    #both product types must reject negative stock without changing it
    try:
        product.update_stock(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative stock should be rejected.")

    assert product.to_dict()["stock"] == 3

    print(
        f"PASS: {product.get_product_id()} accepts valid stock, "
        "replaces stock and rejects negative stock."
    )

def main() -> None:
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

    print("=" * 60)
    print("LSP TEST: SAME FUNCTION ACCEPTS BOTH PRODUCT TYPES")
    print("=" * 60)

    #both subclasses work through the same Product parameter
    show_product_details(physical_product)
    print()
    show_product_details(digital_product)

    print("\nLSP TEST: BOTH PRESERVE PRODUCT STOCK BEHAVIOUR")

    test_stock_behaviour(physical_product)
    test_stock_behaviour(digital_product)

    print("\nPOLYMORPHISM TEST: ONE MIXED INVENTORY")

    inventory = Inventory()
    inventory.add_product(physical_product)
    inventory.add_product(digital_product)

    #normal inventory operations work with both product types
    assert inventory.find_product("TEST001") is physical_product
    assert inventory.find_product("TEST002") is digital_product
    assert len(inventory.get_products()) == 2

    products: list[Product] = inventory.get_products()
    fulfilment_messages: list[str] = []

    #one loop calls the same methods without checking the subclass
    for product in products:
        print("-" * 60)
        product.display_information()

        fulfilment_info = product.get_fulfilment_info()
        assert isinstance(fulfilment_info, str)

        print(fulfilment_info)
        fulfilment_messages.append(fulfilment_info)

    #check that each subclass supplied its own fulfilment behaviour
    assert fulfilment_messages == [
        "This product requires physical shipping.",
        "This product is delivered digitally."
    ]

    print("\nPASS: Both product types work in the same inventory.")
    print("PASS: One loop invokes the correct subclass methods.")
    print("All LSP and polymorphism tests passed.")

if __name__ == "__main__":
    main()