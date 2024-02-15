from ..base import *
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
        input: str,
        model: str,
        mask: str = '[MASK]',
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPFillModel:
        try:
            response = self.client.post(
                url=f'/{model}',
                json={
                    'inputs': input.replace('[#]', mask),
                    'options': {
                        'use_cache': use_cache,
                        'wait_for_model': wait_for_model
                    }
                }
            )

            if response.status_code == 200:
                return NLPFillModel.from_json(response.json())
            else:
                self.raise_error_based_on(
                    status_code=response.status_code
                )
        except:
            raise IntellectoUnknownError()

    def summarise(
        self,
        model: str
    ) -> NLPSummariseModel:
        pass

    def qna(
        self,
        model: str,
        question: str,
        context: str,
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPQnaModel:
        try:
            response = self.client.post(
                url=f'/{model}',
                json={
                    'inputs': {
                        'question': question,
                        'context': context
                    },
                    'options': {
                        'use_cache': use_cache,
                        'wait_for_model': wait_for_model
                    }
                }
            )

            if response.status_code == 200:
                return NLPQnaModel.from_json(response.json())
            else:
                self.raise_error_based_on(
                    status_code=response.status_code
                )
        except:
            raise IntellectoUnknownError()

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
