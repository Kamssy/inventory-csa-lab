"""Main script: reads the inventory and calculates total stock value."""

from inventory import inventory
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(items):
    total = 0
    for item in items:
        total += item["price"]
    return total


def main():
    print("Inventory Report")
    for item in inventory:
        print(item["item_name"], item["quantity"], item["price"])

    print("Total stock value:", total_stock_value(inventory))
    print("Highest stock:", highest_stock_item(inventory)["item_name"])
    print("Lowest stock:", lowest_stock_item(inventory)["item_name"])


if __name__ == "__main__":
    main()