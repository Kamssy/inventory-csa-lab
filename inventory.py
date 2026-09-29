from dataclasses import dataclass
@dataclass
class Item:
    """One inventory item."""

    item_name: str
    quantity: int
    price: float


inventory: list[Item] = [
    Item("Notebook", 50, 500),
    Item("Pen", 200, 100),
    Item("Stapler", 15, 1200),
    Item("Marker", 0, 350),
]