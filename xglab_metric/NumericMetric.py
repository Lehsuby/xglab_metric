from abc import abstractmethod, ABCMeta
from typing import List

from xglab_metric.Event import Event
from xglab_metric.ValuedEvent import ValuedEvent


class NumericMetric:
    __metaclass__ = ABCMeta

    def __init__(self, metric_id: int):
        self.metric_id = metric_id

    @abstractmethod
    def rates(self, events: List[Event]) -> List[ValuedEvent]:
        """ Calculate metric for event """
