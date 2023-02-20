from enum import auto
from strenum import StrEnum


class TeamValueStrategyType(StrEnum):
    KeepValue = auto()
    TotalProbability = auto()
