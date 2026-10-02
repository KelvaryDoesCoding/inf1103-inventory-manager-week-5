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


        elif option == "6":

            print("\nSaving inventory before exit...")


            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")

            break

        else:

            print("\nInvalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()