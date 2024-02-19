from typing import Any
from dataclasses import dataclass

from ...base import IntellectoModel


@dataclass
class NLPSummariseModel(IntellectoModel):
    summary_text: str

    @staticmethod
    def from_json(json: Any) -> 'NLPSummariseModel':
        return NLPSummariseModel(**json)
