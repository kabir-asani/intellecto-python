from typing import Any
from dataclasses import dataclass

from ...base import IntellectoModel


@dataclass
class NLPRecogniseModel(IntellectoModel):
    entity_group: str
    score: float
    word: str
    start: int
    end: int

    @staticmethod
    def from_json(json: Any) -> 'NLPRecogniseModel':
        return NLPRecogniseModel(**json)
