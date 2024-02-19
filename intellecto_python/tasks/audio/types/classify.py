from typing import Any
from dataclasses import dataclass
from ...base import IntellectoModel


@dataclass
class AudioClassifyModel(IntellectoModel):
    score: float
    label: str

    @staticmethod
    def from_json(json: Any) -> 'AudioClassifyModel':
        return AudioClassifyModel(**json)
