from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    products_cart: dict
    location: list[int]
    money: int
    car: object

    def go_to_location(self, location: list[int]) -> None:
        self.home = self.location
        self.location = location

    def go_home(self) -> None:
        self.location = self.home
