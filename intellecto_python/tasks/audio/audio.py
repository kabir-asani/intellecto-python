from .types import *


class IntellectoAudio(IntellectoBase):
    def __init__(
        self,
        token: str
    ) -> None:
        """Construct a new synchronous intellecto audio instance.
        """

        super().__init__(
            token=token
        )

    def transcribe(
        self,
        model: str
    ) -> AudioTranscribeModel:
        pass

    def classify(
        self,
        model: str
    ) -> AudioClassifyModel:
        pass


class AsyncIntellectoAudio(AsyncIntellectoBase):
    def __init__(
        self,
        token: str
    ) -> None:
        """Construct a new asynchronous intellecto audio instance.
        """

        super().__init__(
            token=token
        )

    async def transcribe(
        self,
        model: str
    ) -> AudioTranscribeModel:
        pass

    async def classify(
        self,
        model: str
    ) -> AudioClassifyModel:
        pass
