from dataclasses import dataclass
import datetime


@dataclass
class Customer:
    name: str
    address: str
    email: str


@dataclass
class Phone:
    brand: str
    model: str
    price: float
    serial_number: str


@dataclass
class Plan:
    customer: Customer
    phone: Phone
    start_date: datetime.date
    total_number_months: int
    monthly_price: float
    phone_included: bool
