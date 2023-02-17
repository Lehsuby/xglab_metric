from typing import TypedDict, Optional

from xglab_metric.PlayerMetricRow import PlayerMetricRow


class EventInfo(TypedDict):
    uuid: str
    matchId: int
    teamId: int
    playerId: Optional[int]
    order: int
    dependentChainId: int


class ValuedEvent:
    def __init__(
            self,
            event_info: EventInfo,
            value: float,
            team_value: float,
            class_name: str,
            metric_id: int
    ):
        self.event_info = event_info
        self.value = value
        self.team_value = team_value
        self.class_name = class_name
        self.metric_id = metric_id

    def to_row(self) -> PlayerMetricRow:
        player_id = self.event_info['playerId']
        if player_id is None:
            raise Exception(f"Event {self.event_info['uuid']} should have player id")

        return {
            "metricId": self.metric_id,
            "eventUuid": self.event_info['uuid'],
            "teamId": self.event_info['teamId'],
            "matchId": self.event_info['matchId'],
            "playerId": player_id,
            "className": self.class_name,
            "value": self.value,
            "teamValue": self.team_value
        }
