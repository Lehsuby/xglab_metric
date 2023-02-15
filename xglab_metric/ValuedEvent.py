from xglab_metric.Event import Event
from xglab_metric.PlayerMetricRow import PlayerMetricRow


class ValuedEvent:
    def __init__(
            self,
            event: Event,
            value: float,
            team_value: float,
            class_name: str,
            metric_id: int
    ):
        self.event = event
        self.value = value
        self.team_value = team_value
        self.class_name = class_name
        self.metric_id = metric_id

    def to_row(self) -> PlayerMetricRow:
        player_id = self.event['playerId']
        if player_id is None:
            raise Exception(f"Event {self.event['uuid']} should have player id")

        return {
            "metricId": self.metric_id,
            "eventUuid": self.event['uuid'],
            "teamId": self.event['teamId'],
            "matchId": self.event['matchId'],
            "playerId": player_id,
            "className": self.class_name,
            "value": self.value,
            "teamValue": self.team_value
        }
