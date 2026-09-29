from inventory import Item, inventory
from utils.helpers import highest_stock_item, lowest_stock_item

LOW_STOCK_LIMIT = 20

def total_stock_value(items: list[Item]) -> float:
    total = 0
    for item in items:
        total += item.quantity * item.price
    return total


def print_report(items: list[Item]) -> None:
    """Print the inventory as an aligned table with a low-stock warning."""
    print(f"{'Item':<12}{'Qty':>6}{'Price':>10}{'Value':>12}  Status")
    print("-" * 50)
    for item in items:
        value = item.quantity * item.price
        status = "LOW STOCK" if item.quantity < LOW_STOCK_LIMIT else "OK"
        print(
            f"{item.item_name:<12}{item.quantity:>6}"
            f"{item.price:>10,.2f}{value:>12,.2f}  {status}"
        )

def main() -> None:
    print("=== Inventory Report ===")
    print_report(inventory)
    print()

    print(f"Total stock value: {total_stock_value(inventory):,.2f}")
    print(f"Highest stock: {highest_stock_item(inventory).item_name}")
    print(f"Lowest stock:  {lowest_stock_item(inventory).item_name}")

if __name__ == "__main__":
    main() 
