import random
import string
from datetime import datetime, date
from typing import Iterable


def generate_id(length: int) -> str:
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )


def weekday() -> str:
    today = datetime.today()
    return f"{today:%A}"


def main() -> None:
    print(f"Today is a {weekday()}")
    print(f"Your id = {generate_id(10)}")


####################


def weekday_pure(day: date) -> str:
    return f"{day:%A}"


def generate_id_pure(characters: Iterable[str]) -> str:
    return "".join(characters)


def main_pure() -> None:

    today = datetime.today()
    print(f"Today is a {weekday_pure(today)}")

    length = 10
    random_chars = generate_id_pure(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )
    print(f"Your id = {random_chars}")


if __name__ == "__main__":
    main_pure()
