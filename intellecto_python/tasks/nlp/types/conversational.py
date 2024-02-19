from typing import Any, List, Dict
from dataclasses import dataclass
from ...base import IntellectoModel


@dataclass
class NLPConversationalModel(IntellectoModel):
    generated_text: str
    conversation: Dict[str, List[str]]

    @staticmethod
    def from_json(json: Any) -> 'NLPConversationalModel':
        return NLPConversationalModel(**json)
