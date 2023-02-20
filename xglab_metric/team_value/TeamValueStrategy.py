from abc import ABC, abstractmethod
from typing import List, Dict

from xglab_metric.ValuedEvent import ValuedEvent


class TeamValueStrategy(ABC):

    @staticmethod
    @abstractmethod
    def get_team_value_map(valued_events: List[ValuedEvent]) -> Dict[str, float]:
        raise NotImplementedError
