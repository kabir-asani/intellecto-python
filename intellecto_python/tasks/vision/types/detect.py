from typing import Any
from dataclasses import dataclass
from ...base import IntellectoModel


@dataclass
class VisionDetectBoundingBoxModel:
    xmin: float
    ymin: float
    xmax: float
    ymax: float

    @staticmethod
    def from_json(json: Any) -> 'VisionDetectBoundingBoxModel':
        return VisionDetectBoundingBoxModel(**json)


@dataclass
class VisionDetectModel(IntellectoModel):
    score: float
    label: str
    box: VisionDetectBoundingBoxModel

    @staticmethod
    def from_json(json: Any) -> 'VisionDetectModel':
        return VisionDetectModel(**json)
