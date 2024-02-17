from typing import Any
from dataclasses import dataclass
from ...base import IntellectoBase


@dataclass
class NLPSummariseModel(IntellectoBase):
    summary_text: str

    @staticmethod
    def from_json(json: Any) -> 'NLPFillModel':
        summary_text = str(json.get('summary_text'))

        return NLPSummariseModel(
            summary_text=summary_text
        )
