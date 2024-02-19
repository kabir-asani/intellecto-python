from typing import Any
from dataclasses import dataclass
from ...base import IntellectoModel


@dataclass
class VisionClassifyModel(IntellectoModel):
    score: float
    label: str

    @staticmethod
    def from_json(json: Any) -> 'VisionClassifyModel':
        return VisionClassifyModel(**json)
