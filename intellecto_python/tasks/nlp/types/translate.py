from typing import Any
from dataclasses import dataclass
from ...base import IntellectoBase


@dataclass
class NLPTranslateModel(IntellectoBase):
    translation_text: str

    @staticmethod
    def from_json(json: Any) -> 'NLPTranslateModel':
        return NLPTranslateModel(**json)
