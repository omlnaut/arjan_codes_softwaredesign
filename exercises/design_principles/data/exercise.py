from dataclasses import dataclass, field
from enum import Enum, auto


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


@dataclass
class Item:
    name: str
    quantity: int
    price: int

    @property
    def total_price(self) -> int:
        return self.quantity * self.price


@dataclass
class Order:
    items: list[Item] = field(default_factory=list)
    status: str = "open"

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    @property
    def total_price(self) -> int:
        return sum(item.total_price for item in self.items)


def main() -> None:
    order = Order()
    order.add_item(Item("Keyboard", 1, 5000))
    order.add_item(Item("SSD", 1, 15000))
    order.add_item(Item("USB cable", 2, 500))

    print(f"The total price is: ${(order.total_price / 100):.2f}.")


if __name__ == "__main__":
    main()
