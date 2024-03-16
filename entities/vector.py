from dataclasses import dataclass
from typing import Tuple


@dataclass
class Vector:
    value: Tuple[int, int]

    @property
    def x(self) -> int:
        return self.value[0]

    @property
    def y(self) -> int:
        return self.value[1]
