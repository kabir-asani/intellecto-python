from dataclasses import dataclass
from typing import Any
from ...base import IntellectoModel


@dataclass
class NLPClassifyModel(IntellectoModel):
    label: str
    score: float

    @staticmethod
    def from_json(json: Any) -> 'NLPClassifyModel':
        return NLPClassifyModel(**json)
