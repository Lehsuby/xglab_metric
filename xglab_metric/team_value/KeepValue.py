from typing import List, Dict

from xglab_metric.ValuedEvent import ValuedEvent
from xglab_metric.team_value.TeamValueStrategy import TeamValueStrategy


class KeepValue(TeamValueStrategy):
    @staticmethod
    def get_team_value_map(valued_events: List[ValuedEvent]) -> Dict[str, float]:
        team_value_map: Dict[str, float] = {}
        for ve in valued_events:
            team_value_map[ve.event_info['uuid']] = ve.value
        return team_value_map
