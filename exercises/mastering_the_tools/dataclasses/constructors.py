from dataclasses import dataclass, field

# old
class OldA:
    def __init__(self) -> None:
        self._length = 0


class OldB:
    def __init__(self, x: int, y: str = "hello", l: list[int] | None = None) -> None:
        self.x = x
        self.y = y
        self.l = [] if not l else l


class OldC:
    def __init__(self, a: int = 3) -> None:
        self.a = a
        self.b = a + 3


# new


@dataclass
class A:
    _length: int = 0


@dataclass
class B:
    x: int
    y: str = "hello"
    l: list[int] | None = field(default_factory=list)


@dataclass
class C:
    a: int = 3
    b: int = field(init=False)

    def __post_init__(self):
        self.b = self.a + 3
