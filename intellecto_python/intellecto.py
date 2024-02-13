from .tasks import *


class Intellecto:
    nlp: IntellectoNLP
    audio: IntellectoAudio
    vision: IntellectoVision

    def __init__(
        self,
        access_token: str
    ) -> None:
        self.nlp = IntellectoNLP(
            token=access_token
        )
        self.audio = IntellectoAudio(
            token=access_token
        )
        self.vision = IntellectoVision(
            token=access_token
        )


class AsyncIntellecto:
    nlp: AsyncIntellectoNLP
    audio: AsyncIntellectoAudio
    vision: AsyncIntellectoVision

    def __init__(
        self,
        access_token: str
    ) -> None:
        self.nlp = AsyncIntellectoNLP(
            token=access_token
        )
        self.audio = AsyncIntellectoAudio(
            token=access_token
        )
        self.vision = AsyncIntellectoVision(
            token=access_token
        )
