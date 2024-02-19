from typing import Any, List, Dict, Literal
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
        model: str,
        # inputs
        input: str,
        # options
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPFillModel | List[NLPFillModel]:
        try:
            with self.client() as client:
                response = client.post(
                    url=f'/{model}',
                    json={
                        'inputs': input,
                        'options': {
                            'use_cache': use_cache,
                            'wait_for_model': wait_for_model
                        }
                    }
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        NLPFillModel.from_json(data) for data in json
                    ]
                else:
                    return NLPFillModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def summarise(
        self,
        model: str,
        # inputs
        input: str,
        # parameters
        min_length: int | None = None,
        max_legnth: int | None = None,
        top_k: int | None = None,
        top_p: int | None = None,
        temperature: float = 1.0,
        repetition_penalty: float | None = None,
        max_time: float | None = None,
        #  options
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPSummariseModel | List[NLPSummariseModel]:
        try:
            with self.client() as client:
                response = client.post(
                    url=f'/{model}',
                    json={
                        'inputs': input,
                        'parameters': {
                            'min_length': min_length,
                            'max_length': max_legnth,
                            'top_k': top_k,
                            'top_p': top_p,
                            'temperature': temperature,
                            'repetition_penalty': repetition_penalty,
                            'max_time': max_time,
                        },
                        'options': {
                            'use_cache': use_cache,
                            'wait_for_model': wait_for_model
                        }
                    }
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        NLPSummariseModel.from_json(data) for data in json
                    ]
                else:
                    return NLPSummariseModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def qna(
        self,
        model: str,
        # inputs
        question: str,
        context: str,
        # options
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPQnaModel | List[NLPQnaModel]:
        try:
            with self.client() as client:
                response = client.post(
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

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        NLPQnaModel.from_json(data) for data in json
                    ]
                else:
                    return NLPQnaModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def table(
        self,
        model: str,
        # inputs
        query: str,
        table: Dict[str, List[Any]],
        # options
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPTableModel | List[NLPTableModel]:
        try:
            with self.client() as client:
                response = client.post(
                    url=f'/{model}',
                    json={
                        'inputs': {
                            'query': query,
                            'table':  table
                        },
                        'options': {
                            'use_cache': use_cache,
                            'wait_for_model': wait_for_model
                        }
                    }
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        NLPTableModel.from_json(data) for data in json
                    ]
                else:
                    return NLPTableModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def similarity(
        self,
        model: str,
        # inputs
        source_sentence: str,
        sentences: List[str],
        # options
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPSimilarityModel | List[NLPSimilarityModel]:
        try:
            with self.client() as client:
                response = client.post(
                    url=f'/{model}',
                    json={
                        'inputs': {
                            'source_sentence': source_sentence,
                            'sentences': sentences
                        },
                        'options': {
                            'use_cache': use_cache,
                            'wait_for_model': wait_for_model
                        }
                    }
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        float(data) for data in json
                    ]
                else:
                    return float(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def classify(
        self,
        model: str,
        # inputs
        input: str,
        # options
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPClassifyModel | List[NLPClassifyModel]:
        try:
            with self.client() as client:
                response = client.post(
                    url=f'/{model}',
                    json={
                        'inputs': input,
                        'options': {
                            'use_cache': use_cache,
                            'wait_for_model': wait_for_model
                        }
                    }
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        NLPClassifyModel.from_json(data) for data in json
                    ]
                else:
                    return NLPClassifyModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def generate(
        self,
        model: str,
        # inputs
        input: str,
        # parameters
        top_k: int | None = None,
        top_p: float | None = None,
        temperature: float = 1.0,
        repetition_penalty: float | None = None,
        max_new_tokens: int | None = None,
        max_time: float | None = None,
        return_full_text: bool = True,
        num_return_sequences: int = 1,
        do_sample: bool = True,
        # options
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPGenerateModel | List[NLPGenerateModel]:
        try:
            with self.client() as client:
                response = client.post(
                    url=f'/{model}',
                    json={
                        'inputs': input,
                        'parameters': {
                            'top_k': top_k,
                            'top_p': top_p,
                            'temperature': temperature,
                            'repetition_penalty': repetition_penalty,
                            'max_new_tokens': max_new_tokens,
                            'max_time': max_time,
                            'return_full_text': return_full_text,
                            'num_return_sequences': num_return_sequences,
                            'do_sample': do_sample,
                        },
                        'options': {
                            'use_cache': use_cache,
                            'wait_for_model': wait_for_model
                        }
                    }
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        NLPGenerateModel.from_json(data) for data in json
                    ]
                else:
                    NLPGenerateModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def recognise(
        self,
        model: str,
        # inputs
        input: str,
        # parameters
        aggregation_strategy: Literal[
            'none',
            'simple',
            'first',
            'average',
            'max'
        ] = 'simple',
        # options
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPRecogniseModel | List[NLPRecogniseModel]:
        try:
            with self.client() as client:
                response = client.post(
                    url=f'/{model}',
                    json={
                        'inputs': input,
                        'parameters': {
                            'aggregation_strategy': aggregation_strategy,
                        },
                        'options': {
                            'use_cache': use_cache,
                            'wait_for_model': wait_for_model
                        }
                    }
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        NLPRecogniseModel.from_json(data) for data in json
                    ]
                else:
                    return NLPRecogniseModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def translate(
        self,
        model: str,
        # inputs
        input: str,
        # options
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPTranslateModel | List[NLPTranslateModel]:
        try:
            with self.client() as client:
                response = client.post(
                    url=f'/{model}',
                    json={
                        'inputs': input,
                        'options': {
                            'use_cache': use_cache,
                            'wait_for_model': wait_for_model
                        }
                    }
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        NLPTranslateModel.from_json(data) for data in json
                    ]
                else:
                    return NLPTranslateModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def zero_shot_classify(
        self,
        model: str,
        # inputs
        input: str,
        # parameters
        candidate_labels: List[str],
        multi_label: bool = False,
        # options
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPZeroShotClassifyModel | List[NLPZeroShotClassifyModel]:
        try:
            with self.client() as client:
                response = client.post(
                    url=f'/${model}',
                    json={
                        'inputs': input,
                        'parameters': {
                            'candidate_labels': candidate_labels,
                            'multi_label': multi_label
                        },
                        'options': {
                            'use_cache': use_cache,
                            'wait_for_model': wait_for_model
                        }
                    }
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        NLPZeroShotClassifyModel.from_json(data) for data in json
                    ]
                else:
                    return NLPZeroShotClassifyModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def conversational(
        self,
        model: str,
        # inputs
        text: str,
        past_user_inputs: List[str] = [],
        generated_responses: List[str] = [],
        # parameters
        min_length: int | None = None,
        max_length: int | None = None,
        top_k: int | None = None,
        top_p: int | None = None,
        temperature: int = 1.0,
        repetition_penalty: float | None = None,
        max_time: float | None = None,
        # options
        use_cache: bool = True,
        wait_for_model: bool = False
    ) -> NLPConversationalModel | List[NLPConversationalModel]:
        try:
            with self.client() as client:
                response = client.post(
                    url=f'/${model}',
                    json={
                        'inputs': input,
                        'parameters': {
                            'min_length': min_length,
                            'max_length': max_length,
                            'top_k': top_k,
                            'top_p': top_p,
                            'temperature': temperature,
                            'repetition_penalty': repetition_penalty,
                            'max_time': max_time
                        },
                        'options': {
                            'use_cache': use_cache,
                            'wait_for_model': wait_for_model
                        }
                    }
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        NLPConversationalModel.from_json(data) for data in json
                    ]
                else:
                    return NLPConversationalModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()
