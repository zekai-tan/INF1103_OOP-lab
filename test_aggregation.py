from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory


def main() -> None:
    #create the supplier and product before creating the inventories
    supplier = Supplier(
        "S001",
        "Tech Supplier",
        "supplier@example.com"
    )

    product = PhysicalProduct(
        "TEST001",
        "Test Laptop",
        1200.0,
        5,
        2.2,
        supplier
    )

    inventory_a = Inventory()
    inventory_b = Inventory()

    #add the existing product to inventory A
    inventory_a.add_product(product)

    assert inventory_a.find_product("TEST001") is product
    print("Product added to Inventory A.")

    #remove the product reference from inventory A
    removed_product = inventory_a.remove_product("TEST001")

    assert removed_product is product
    assert inventory_a.find_product("TEST001") is None

    print("\nProduct removed from Inventory A.")

    #the original product still works after removal
    product.display_information()

    #add the same product object to inventory B
    inventory_b.add_product(product)

    assert inventory_b.find_product("TEST001") is product
    print("\nThe same product object is now in Inventory B.")

    #a missing product should return None
    assert inventory_a.remove_product("MISSING") is None

    print("\nAll aggregation tests passed.")


if __name__ == "__main__":
    main()