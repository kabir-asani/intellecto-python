from ..base import IntellectoBase, IntellectoModel
from .types import *


class IntellectoNLP(IntellectoBase):
    def __init__(
        self,
        token: str
    ) -> None:
        """Construct a new synchronous intellecto NLP instance.
        """

        super().__init__(
            token=token
        )

    def fill(
        self,
        model: str
    ) -> NLPFillModel:
        pass

    def summarise(
        self,
        model: str
    ) -> NLPSummariseModel:
        pass

    def qna(
        self,
        model: str
    ) -> NLPQnaModel:
        pass

    def table(
        self,
        model: str
    ) -> NLPTableModel:
        pass

    def similarity(
        self,
        model: str
    ) -> NLPSimilarityModel:
        pass

    def classify(
        self,
        model: str
    ) -> NLPClassifyModel:
        pass

    def generate(
        self,
        model: str
    ) -> NLPGenerateModel:
        pass

    def recognise(
        self,
        model: str
    ) -> NLPRecogniseModel:
        pass

    def translate(
        self,
        model: str
    ) -> NLPTranslateModel:
        pass

    def zero_shot_classify(
        self,
        model: str
    ) -> NLPZeroShotClassifyModel:
        pass

    def conversational(
        self,
        model: str
    ) -> NLPConversationalModel:
        pass

    def feature_extract(
        self,
        model: str
    ) -> NLPFeatureExtractModel:
        pass


class AsyncIntellectoNLP(AsyncIntellectoBase):
    def __init__(
        self,
        model: str,
        token: str
    ) -> None:
        """Construct a new asynchronous intellecto NLP instance.
        """

        super().__init__(
            model=model,
            token=token
        )

    async def fill(
        self,
        model: str
    ) -> NLPFillModel:
        pass

    async def summarise(
        self,
        model: str
    ) -> NLPSummariseModel:
        pass

    async def qna(
        self,
        model: str
    ) -> NLPQnaModel:
        pass

    async def table(
        self,
        model: str
    ) -> NLPTableModel:
        pass

    async def similarity(
        self,
        model: str
    ) -> NLPSimilarityModel:
        pass

    async def classify(
        self,
        model: str
    ) -> NLPClassifyModel:
        pass

    async def generate(
        self,
        model: str
    ) -> NLPGenerateModel:
        pass

    async def recognise(
        self,
        model: str
    ) -> NLPRecogniseModel:
        pass

    async def translate(
        self,
        model: str
    ) -> NLPTranslateModel:
        pass

    async def zero_shot_classify(
        self,
        model: str
    ) -> NLPZeroShotClassifyModel:
        pass

    async def conversational(
        self,
        model: str
    ) -> NLPConversationalModel:
        pass

    async def feature_extract(
        self,
        model: str
    ) -> NLPFeatureExtractModel:
        pass
