import json

#import the classes created
from product import Product
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from shipping import CanBeShipped


def load_inventory():
    #load the inventory from a JSON file and return an Inventory object

    try:
        #read saved inventory from the current working folder.
        with open("inventory.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("inventory.json not found. Starting with a empty inventory.")
        return Inventory()

    #json file must have a list of product dictionaries
    if not isinstance(data, list):
        raise ValueError("inventory.json must have a list of products.")

    inventory = Inventory()

    for item in data:
        #check that each saved product is a dictionary
        if not isinstance(item, dict):
            raise ValueError("Each saved product must be a dictionary.")

        #read the saved product type
        product_type = item.get("type")

        #convert each dictionary into a product object
        if product_type == "physical":
            product = PhysicalProduct(
                item["id"],
                item["name"],
                item["price"],
                item["stock"],
                item["weight"]
            )

        elif product_type == "digital":
            product = DigitalProduct(
                item["id"],
                item["name"],
                item["price"],
                item["stock"],
                item["download_size"]
            )

        else:
            #reject missing or invalid product types
            raise ValueError(
                f"Product {item.get('id', '(unknown)')} must have "
                "a type of 'physical' or 'digital'."
            )

        #manage adding and checking for duplicate IDds
        inventory.add_product(product)

    print("inventory.json found.")
    print("Inventory loaded.")
    return inventory


def save_inventory(inventory):
    #convert the list of Product objects into a list of dictionaries so JSON can store
    data = [
        product.to_dict()
        for product in inventory.get_products()
    ]
    try:
        #write the current inventory replacing previous file content
        with open("inventory.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError as error:
        #returning false allows the program to keep running and avoid exiting without saving
        print(f"Inventory cannot be saved: {error}")
        return False

    print("Inventory saved to inventory.json.")
    return True


def add_product_from_input(inventory):

    print("\nAdd New Product")

    #select which type of product to add
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Select product type: ").strip()
    if product_type not in ("1", "2"):
        print("Invalid product type. Please select 1 or 2.")
        return

    #remove leading/trailing spaces and convert to uppercase for consistency
    product_id = input("Product ID: ").strip().upper()

    #reject duplicate IDs
    if inventory.search_product(product_id) is not None:
        print("A product with this ID already exists.")
        return
    
    name = input("Product Name: ").strip()
    try:
        #convert to float and int
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())

        if product_type == "1":
            #collect the weight for a physical product
            weight = float(input("Weight (kg): ").strip())

            product = PhysicalProduct(
                product_id,
                name,
                price,
                stock,
                weight
            )

        else:
            #collect the download size for a digital product
            download_size = float(input("Download Size (MB): ").strip())
            product = DigitalProduct(
                product_id,
                name,
                price,
                stock,
                download_size
            )
        inventory.add_product(product)
    except ValueError as error:
        #handle invalid numeric input or rejected product attributes
        print(f"Product was not added: {error}")
        return

    print("Product added")


def update_stock_from_input(inventory):

    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return

    print("\nProduct Found:")
    product.display_information()

    try:
        quantity = int(input("New Stock Quantity: ").strip())
        #replaces the current stck...not add
        product.update_stock(quantity)
    except ValueError as error:
        print(f"Stock wasn't updated: {error}")
        return
    print("Stock updated")


def search_product_from_input(inventory):

    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return
    print("\nProduct Found")
    print("-" * 72)

    #product object display its own information
    product.display_information()

    #display how the product is delivered
    print(f"Fulfilment: {product.get_fulfilment_info()}")

    #only calculate shipping for products that can be shipped
    if isinstance(product, CanBeShipped):
        print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
    print("-" * 72)


def show_menu():

    print("""
----------- MENU -----------
1. Display All Products
2. Add Product
3. Update Stock
4. Search Product
5. Save Inventory
6. Exit
----------------------------
""")


def main():
    
    print("=" * 40)
    print("OOP INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    try:
        #restore saved products before displaying the menu
        inventory = load_inventory()

    except (OSError, ValueError, KeyError, TypeError) as error:
        #stop if existing file is unreadable/contain invalid data
        #so an empty inventory is not created and saved over the existing file
        print(f"Could not load inventory: {error}")
        print("Program ceased to avoid overwriting existing data.")
        return

    #keep showing the menu until user successfully saves and exits
    while True:
        show_menu()
        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_all()

        elif option == "2":
            add_product_from_input(inventory)

        elif option == "3":
            update_stock_from_input(inventory)

        elif option == "4":
            search_product_from_input(inventory)

        elif option == "5":
            #save without leaving the menu
            print("Saving inventory")
            save_inventory(inventory)

        elif option == "6":
            print("Saving inventory before exiting")

            if save_inventory(inventory):
                print("Thankyou for using the programme")
                print("Program ceased.")
                break

            print("Exit cancelled due to saving failure.")

        else:
            print("Invalid option. Please enter a number from 1 to 6.")


#start the application only when this file is run directly.
if __name__ == "__main__":
    main()