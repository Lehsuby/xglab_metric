from typing import TypedDict


class PlayerMetricRow(TypedDict):
    eventUuid: str
    matchId: int
    teamId: int
    playerId: int
    metricId: int
    className: str
    value: float
    teamValue: float
