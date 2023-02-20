from abc import abstractmethod, ABCMeta
from typing import List

from xglab_metric.Event import Event
from xglab_metric.PlayerMetricRow import PlayerMetricRow
from xglab_metric.ValuedEvent import ValuedEvent
from xglab_metric.team_value import strategy_selector
from xglab_metric.team_value.TeamValueStrategyType import TeamValueStrategyType


class NumericMetric:
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def team_value_strategy(self) -> TeamValueStrategyType:
        """ Calculate metric for event """

    def __init__(self, metric_id: int):
        self.metric_id = metric_id

    @abstractmethod
    def evaluate(self, events: List[Event]) -> List[ValuedEvent]:
        """ Calculate metric for event """

    def metric_rows(self, events: List[Event]) -> List[PlayerMetricRow]:
        valued = self.evaluate(events)
        team_value_map = strategy_selector.get_team_value_map(self.team_value_strategy, valued)
        rows: List[PlayerMetricRow] = [v.to_row(self.metric_id, team_value_map[v.event_info['uuid']]) for v in valued]
        return rows
