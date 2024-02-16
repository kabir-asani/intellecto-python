from ..base import IntellectoBase, AsyncIntellectoBase
from .types import *


class IntellectoVision(IntellectoBase):
    def __init__(
        self,
        token: str
    ) -> None:
        """Construct a new synchronous intellecto vision instance.
        """

        super().__init__(
            token=token
        )

    def classify(
        self,
        model: str
    ) -> VisionClassifyModel:
        pass

    def detect(
        self,
        model: str
    ) -> VisionDetectModel:
        pass


class AsyncIntellectoVision(AsyncIntellectoBase):
    def __init__(
        self,
        token: str
    ) -> None:
        """Construct a new asynchronous intellecto vision instance.
        """

        super().__init__(
            token=token
        )

    async def classify(
        self,
        model: str
    ) -> VisionClassifyModel:
        pass

    async def detect(
        self,
        model: str
    ) -> VisionDetectModel:
        pass
