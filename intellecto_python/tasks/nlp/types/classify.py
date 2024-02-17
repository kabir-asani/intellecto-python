from dataclasses import dataclass
from typing import Any
from ...base import IntellectoBase


@dataclass
class NLPClassifyModel(IntellectoBase):
    label: str
    score: float

    @staticmethod
    def from_json(json: Any) -> 'NLPClassifyModel':
        return NLPClassifyModel(**json)
