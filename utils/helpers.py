from inventory import Item


def highest_stock_item(items: list[Item]) -> Item:
    """Return the item with the highest quantity."""
    return max(items, key=lambda item: item.quantity)


def lowest_stock_item(items: list[Item]) -> Item:
    """Return the item with the lowest quantity."""
    return min(items, key=lambda item: item.quantity)