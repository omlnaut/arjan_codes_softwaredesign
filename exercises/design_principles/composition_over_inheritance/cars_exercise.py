from dataclasses import dataclass
from enum import Enum, auto
from typing import Protocol


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


class RentInformation(Protocol):
    brand: str
    model: str
    reserved: bool


class CarInformation(Protocol):
    color: str
    fuel_type: FuelType
    license_plate: str


class PaymentProcessor(Protocol):
    def compute_total_price(self, value: int) -> int:
        ...


@dataclass
class Vehicle:
    rent_information: RentInformation
    car_information: CarInformation
    payment_processor: PaymentProcessor


####### PaymentProcessors ###########


@dataclass
class PerDayPayment:
    price_per_day: int

    def compute_total_price(self, days: int):
        return self.price_per_day * days


@dataclass
class PerKilometerPayment:
    price_per_kilometer: int

    def compute_total_price(self, kilometer: int):
        return self.price_per_kilometer * kilometer


@dataclass
class PerMonthPayment:
    price_per_month: int

    def compute_total_price(self, month: int):
        return self.price_per_month * month


####### PaymentProcessors ###########


@dataclass
class CarPerDay(Vehicle):
    price_per_km: int
    price_per_day: int
    number_of_seats: int
    storage_capacity_litres: int


@dataclass
class CarPerMonth(Vehicle):
    price_per_month: int

    number_of_seats: int
    storage_capacity_litres: int


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle


@dataclass
class Trailer(Rentable):
    capacity_m3: int
    price_per_month: int


def main():
    pass


if __name__ == "__main__":
    main()
