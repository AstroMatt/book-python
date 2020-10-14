"""
>>> position = Position()
>>> position
Position(x=0, y=0)
>>> position @ (1,2)
>>> position
Position(x=1, y=2)
"""
from dataclasses import dataclass


@dataclass
class Position:
    x: int = 0
    y: int = 0

    def __matmul__(self, other: tuple[int, int]) -> None:
        self.x = other[0]
        self.y = other[1]
