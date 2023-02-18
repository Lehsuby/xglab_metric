from typing import List, Dict

from xglab_metric.ValuedEvent import ValuedEvent
from xglab_metric.team_value.TeamValueStrategy import TeamValueStrategy


class TotalProbability(TeamValueStrategy):
    @staticmethod
    def get_team_value_map(valued_events: List[ValuedEvent]) -> Dict[str, float]:
        team_value_map: Dict[str, float] = {}
        events_chains_by_team: Dict[int, Dict[int, List[ValuedEvent | None]]] = {}
        for ve in valued_events:
            team_events_chains: Dict[int, List[ValuedEvent | None]] = events_chains_by_team.get(ve.event_info['teamId'],
                                                                                                {})
            events_chain: List[ValuedEvent | None] = team_events_chains.get(ve.event_info['dependentChainId'], [])
            if len(events_chain) >= ve.event_info['order']:
                events_chain[ve.event_info['order'] - 1] = ve
            else:
                events_chain.append(ve)
                events_chain = sorted(events_chain, key=lambda k: k.event_info['order'])
            team_events_chains.update({ve.event_info['dependentChainId']: events_chain})
            events_chains_by_team.update({ve.event_info['teamId']: team_events_chains})
        for chains_by_team in events_chains_by_team.values():
            for chain in chains_by_team.values():
                prev_probability: float = 0
                for valued_event in chain:
                    probability: float = valued_event.value * (1 - prev_probability)
                    prev_probability = probability
                    team_value_map[valued_event.event_info['uuid']] = probability
        return team_value_map
