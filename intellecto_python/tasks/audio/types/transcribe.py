from typing import Any
from dataclasses import dataclass
from ...base import IntellectoModel


@dataclass
class AudioTranscribeModel(IntellectoModel):
    text: str

    @staticmethod
    def from_json(json: Any) -> 'AudioTranscribeModel':
        return AudioTranscribeModel(**json)
