from typing import Any
from dataclasses import dataclass

from ...base import IntellectoBase


@dataclass
class NLPQnaModel(IntellectoBase):
    answer: str
    score: float
    start: int
    stop: int

    @staticmethod
    def from_json(json: Any) -> 'NLPQnaModel':
        answer = str(json.get('answer'))
        score = str(json.get('score'))
        start = int(json.get('start'))
        stop = str(json.get('stop'))

        return NLPQnaModel(
            answer=answer,
            score=score,
            start=start,
            stop=stop
        )
