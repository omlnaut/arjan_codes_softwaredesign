from dataclasses import dataclass
from typing import Protocol


@dataclass
class VehicleData:
    """A class to hold vehicle data."""

    brand: str
    price_per_day: int
    price_per_km: int


VEHICLE_DATA = {
    "vw": VehicleData(brand="vw", price_per_km=30, price_per_day=6000),
    "bmw": VehicleData(brand="bmw", price_per_km=35, price_per_day=8500),
    "ford": VehicleData(brand="ford", price_per_km=25, price_per_day=12000),
}


class IVehicleRepository(Protocol):
    def get_vehicle_types(self) -> list[str]:
        ...

    def get_vehicle_from_name(self, name: str) -> VehicleData:
        ...


class VehicleRepository:
    def __init__(self):
        self._vehicle_data: dict[str, VehicleData] = {}

    def add_vehicle_data(self, name: str, data: VehicleData) -> None:
        self._vehicle_data[name] = data

    def get_vehicle_types(self) -> list[str]:
        return list(self._vehicle_data.keys())

    def get_vehicle_from_name(self, name: str) -> VehicleData:
        return self._vehicle_data[name]


def read_vehicle_type(vehicle_repo: IVehicleRepository) -> str:
    """Reads the vehicle type from the user."""
    vehicle_types = vehicle_repo.get_vehicle_types()
    vehicle_type = ""
    while vehicle_type not in vehicle_types:
        vehicle_type = input(
            f"What type of vehicle would you like to rent ({', '.join(vehicle_types)})? "
        )
    return vehicle_type


def read_rent_days() -> int:
    """Reads the number of days from the user."""
    days = 0
    while days < 1:
        days_str = input(
            "How many days would you like to rent the vehicle? (enter a positive number) "
        )
        try:
            days = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return days


def read_kms_to_drive() -> int:
    """Reads the number of kilometers to drive from the user."""
    km = 0
    while km < 1:
        km_str = input(
            "How many kilometers would you like to drive (enter a positive number)? "
        )
        try:
            km = int(km_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return km


def compute_rental_cost(
    vehicle_repo: IVehicleRepository, vehicle_type: str, days: int, km: int
) -> int:
    """Computes the rental cost for a vehicle."""
    vehicle_data = vehicle_repo.get_vehicle_from_name(vehicle_type)
    price_per_km = vehicle_data.price_per_km
    price_per_day = vehicle_data.price_per_day
    paid_kms = max(km - 100, 0)
    return price_per_km * paid_kms + price_per_day * days


def main():
    vehicle_repo = VehicleRepository()
    vehicle_repo.add_vehicle_data(
        "vw", VehicleData(brand="vw", price_per_km=30, price_per_day=6000)
    )
    vehicle_repo.add_vehicle_data(
        "bmw", VehicleData(brand="bmw", price_per_km=35, price_per_day=8500)
    )
    vehicle_repo.add_vehicle_data(
        "ford", VehicleData(brand="ford", price_per_km=25, price_per_day=12000)
    )

    vehicle_type = read_vehicle_type(vehicle_repo)

    days = read_rent_days()

    km = read_kms_to_drive()

    # compute the final rental price
    rental_price = compute_rental_cost(vehicle_repo, vehicle_type, days, km)

    # print the result
    print(f"The total price of the rental is ${(rental_price / 100):.2f}")


if __name__ == "__main__":
    main()
