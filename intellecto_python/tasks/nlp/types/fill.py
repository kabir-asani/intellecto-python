from dataclasses import dataclass

from ...base import IntellectoBase


@dataclass
class NLPFillModel(IntellectoBase):
    sequence: str
    score: float
    token: int
    token_str: str

    @staticmethod
    def from_json(json: Any) -> 'NLPFillModel':
        sequence = str(json.get('sequence'))
        score = str(json.get('score'))
        token = int(obj.get('token'))
        token_str = str(obj.get('token_str'))

        return NLPFillModel(
            score=score,
            sequence=sequence,
            token=token,
            token_str=token_str
        )
