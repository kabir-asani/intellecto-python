from typing import Any
from dataclasses import dataclass

from ...base import IntellectoModel


@dataclass
class NLPGenerateModel(IntellectoModel):
    generated_text: str

    @staticmethod
    def from_json(json: Any) -> 'NLPGenerateModel':
        return NLPGenerateModel(**json)
