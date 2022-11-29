from dataclasses import dataclass


@dataclass
class Laptop:
    machine_name: str = "DULL"

    def install_os(self) -> None:
        print("Installing OS")

    def format_hd(self) -> None:
        print("Formatting the hard drive")

    def create_admin_user(self, password: str) -> None:
        print(f"Creating admin user with password {password}.")


def reset(laptop: Laptop) -> None:
    laptop.format_hd()
    laptop.machine_name = "DULL"
    laptop.install_os()
    laptop.create_admin_user("admin")


if __name__ == "__main__":
    l = Laptop()
    reset(l)
