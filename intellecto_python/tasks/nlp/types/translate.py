from typing import Any
from dataclasses import dataclass

from ...base import IntellectoModel


@dataclass
class NLPTranslateModel(IntellectoModel):
    translation_text: str

    @staticmethod
    def from_json(json: Any) -> 'NLPTranslateModel':
        return NLPTranslateModel(**json)
