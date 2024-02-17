from typing import Any
from dataclasses import dataclass

from ...base import IntellectoBase


@dataclass
class NLPQnaModel(IntellectoBase):
    answer: str
    score: float
    start: int
    stop: int

    @staticmethod
    def from_json(json: Any) -> 'NLPQnaModel':
        return NLPQnaModel(**json)
