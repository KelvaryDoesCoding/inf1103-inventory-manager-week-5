import json

FILE_NAME = "inventory.json"


def load_inventory():

    try:
        with open(FILE_NAME, "r") as file:
            inventory = json.load(file)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

        return inventory

    except FileNotFoundError:

        print("inventory.json not found.")
        print("Starting with empty inventory.")

        return []


def save_inventory(inventory):

    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


def display_products(inventory):

    print("\nCurrent Inventory")
    print("-" * 45)

    for product in inventory:

        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 45)


def generate_product_id(inventory):

    if len(inventory) == 0:
        return "P001"

    last_id = inventory[-1]["id"]

    number = int(last_id[1:])

    number += 1

    return f"P{number:03d}"


def add_product(inventory):

    print("\nAdd New Product")

    product_id = generate_product_id(inventory)

    print(f"Product ID: {product_id}")

    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)

    print("\nProduct added successfully!")


def update_stock(inventory):

    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").upper().strip()

    for product in inventory:

        if product["id"] == product_id:

            print("\nProduct Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            new_stock = int(input("\nNew Stock Quantity: "))

            product["stock"] = new_stock

            print("\nStock updated successfully!")

            return

    print("\nProduct not found.")


def search_product(inventory):

    print("\nSearch Product")

    product_id = input("Enter Product ID: ").upper().strip()

    for product in inventory:

        if product["id"] == product_id:

            print("\nProduct Found")
            print("-" * 40)

            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")

            print("-" * 40)

            return

    print("\nProduct not found.")


def display_menu():

    print("\n---------- MENU ----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------")


def main():

    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    print()

    inventory = load_inventory()

    while True:

        display_menu()

        option = input("\nEnter option: ")

        if option == "1":

            display_products(inventory)

        elif option == "2":

            add_product(inventory)

        elif option == "3":

            update_stock(inventory)

        elif option == "4":

            search_product(inventory)

        elif option == "5":

            print("\nSaving inventory...")

            save_inventory(inventory)

        elif option == "6":

            print("\nSaving inventory before exit...")

            save_inventory(inventory)

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")

            break

        else:

            print("\nInvalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()