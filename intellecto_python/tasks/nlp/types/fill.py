from typing import Any
from dataclasses import dataclass

from ...base import IntellectoBase


@dataclass
class NLPFillModel(IntellectoBase):
    sequence: str
    score: float
    token: int
    token_str: str

    @staticmethod
    def from_json(json: Any) -> 'NLPFillModel':
        return NLPFillModel(**json)
