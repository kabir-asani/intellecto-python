from typing import Any
from dataclasses import dataclass
from ...base import IntellectoBase


@dataclass
class NLPSummariseModel(IntellectoBase):
    summary_text: str

    @staticmethod
    def from_json(json: Any) -> 'NLPSummariseModel':
        return NLPSummariseModel(**json)
