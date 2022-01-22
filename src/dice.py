import abc
import logging
import random
from functools import wraps
from typing import Type, Set, Iterable, Any, cast


class Die(abc.ABC):
    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None:
        ...

    def __repr__(self) -> str:
        return f"{self.face}"


class D4(Die):
    def roll(self) -> None:
        self.face = random.choice((1, 2, 3, 4))


class D6(Die):
    def roll(self) -> None:
        self.face = random.randint(1, 6)


class Dice(abc.ABC):
    def __init__(self, n: int, die_class: Type[Die]) -> None:
        self.dice = [die_class() for _ in range(n)]

    @abc.abstractmethod
    def roll(self) -> None:
        ...

    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice)


class SimpleDice(Dice):
    def roll(self) -> None:
        for d in self.dice:
            d.roll()


class YachtDice(Dice):
    def __init__(self) -> None:
        super().__init__(5, D6)
        self.saved: Set[int] = set()

    def saving(self, positions: Iterable[int]) -> "YachtDice":
        if not all(0 <= n < 6 for n in positions):
            raise ValueError("Invalid position")
        self.saved = set(positions)
        return self

    def roll(self) -> None:
        for n, d in enumerate(self.dice):
            if n not in self.saved:
                d.roll()
            self.saved = set()


class DieM(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None:
        ...


class DDice:
    def __init__(self, *dice_class: Type[Die]) -> None:
        self.dice = [dc() for dc in dice_class]
        self.adjust: int = 0

    def plus(self, adjust: int = 0) -> "DDice":
        self.adjust = adjust
        return self

    def roll(self) -> None:
        for d in self.dice:
            d.roll()

    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice) + self.adjust

    def __add__(self, die_class: Any) -> "DDice":
        if isinstance(die_class, type) and issubclass(die_class, Die):
            new_classes = [type(d) for d in self.dice] + [die_class]
            new = DDice(*new_classes).plus(self.adjust)
            return new
        elif isinstance(die_class, int):
            new_classes = [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(die_class)
            return new
        else:
            return NotImplemented

    def __radd__(self, die_class: Any) -> "DDice":
        if isinstance(die_class, type) and issubclass(die_class, Die):
            new_classes = [die_class] + [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(self.adjust)
            return new
        elif isinstance(die_class, int):
            new_classes = [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(die_class)
            return new
        else:
            return NotImplemented

    def __mul__(self, n: Any) -> "DDice":
        if isinstance(n, int):
            new_classes = [type(d) for d in self.dice for _ in range(n)]
            return DDice(*new_classes).plus(self.adjust)
        else:
            return NotImplemented

    def __rmul__(self, n: Any) -> "DDice":
        if isinstance(n, int):
            new_classes = [type(d) for d in self.dice for _ in range(n)]
            return DDice(*new_classes).plus(self.adjust)
        else:
            return NotImplemented

    def __iadd__(self, die_class: Any) -> "DDice":
        if isinstance(die_class, type) and issubclass(die_class, Die):
            self.dice += [die_class]
            return self
        elif isinstance(die_class, int):
            self.adjust += die_class
            return self
        else:
            return NotImplemented


class DieMeta(abc.ABCMeta):
    def __new__(
            metaclass: Type[type],
            name: str,
            bases: tuple[type, ...],
            namespace: dict[str, Any],
            **kwargs: Any) -> "DieMeta":
        if "roll" in namespace and not getattr(
                namespace["roll"], "__isabstractmethod__", False
        ):
            namespace.setdefault("logger", logging.getLogger((name)))

            original_method = namespace["roll"]

            @wraps(original_method)
            def logged_roll(self: "DieLog") -> None:
                original_method(self)
                self.logger.info(f"Rolled {self.face}")

            namespace["roll"] = logged_roll
        new_object = cast(
            "DieMeta", abc.ABCMeta.__new__(
                metaclass, name, bases, namespace
            )
        )
        return new_object


class DieLog(metaclass=DieMeta):
    logger: logging.Logger

    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None:
        ...

    def __repr__(self) -> str:
        return f"{self.face}"


class D6L(DieLog):
    def roll(self) -> None:
        """Some documentation on D6L"""
        self.face = random.randrange(1, 7)
