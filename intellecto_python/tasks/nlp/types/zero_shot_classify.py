from typing import Any, List
from dataclasses import dataclass
from ...base import IntellectoBase


@dataclass
class NLPZeroShotClassifyModel(IntellectoBase):
    sequence: str
    labels: List[str]
    scores: List[float]

    @staticmethod
    def from_json(json: Any) -> 'NLPZeroShotClassifyModel':
        return NLPZeroShotClassifyModel(**json)
