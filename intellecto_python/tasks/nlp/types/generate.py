from typing import Any
from dataclasses import dataclass

from ...base import IntellectoBase


@dataclass
class NLPGenerateModel(IntellectoBase):
    generated_text: str

    @staticmethod
    def from_json(json: Any) -> 'NLPGenerateModel':
        return NLPGenerateModel(**json)
