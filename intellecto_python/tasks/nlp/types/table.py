from typing import Any, List
from dataclasses import dataclass
from ...base import IntellectoBase


@dataclass
class NLPTableModel(IntellectoBase):
    answer: str
    coordinates: List[List[int]]
    cells: List[str]
    aggregator: str

    @staticmethod
    def from_json(json: Any) -> 'NLPTableModel':
        return NLPTableModel(**json)
