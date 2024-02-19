from typing import Any, List
from dataclasses import dataclass

from ...base import IntellectoModel


@dataclass
class NLPTableModel(IntellectoModel):
    answer: str
    coordinates: List[List[int]]
    cells: List[str]
    aggregator: str

    @staticmethod
    def from_json(json: Any) -> 'NLPTableModel':
        return NLPTableModel(**json)
