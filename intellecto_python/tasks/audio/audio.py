from typing import List
from .types import *
from ..base import *
from ...core import *

from os import PathLike


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
        model: str,
        path: str | PathLike[str]
    ) -> AudioTranscribeModel:
        try:
            with open(path, "rb") as data, self.client() as client:
                response = client.post(
                    url=f'/{model}',
                    content=data
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        AudioTranscribeModel.from_json(data) for data in json
                    ]
                else:
                    return AudioTranscribeModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def classify(
        self,
        model: str,
        path: str | PathLike[str]
    ) -> AudioClassifyModel:
        try:
            with open(path, "rb") as data, self.client() as client:
                response = client.post(
                    url=f'/{model}',
                    content=data
                )

                if response.status_code != 200:
                    self.raise_error(
                        status_code=response.status_code
                    )

                json = response.json()

                if isinstance(json, List):
                    return [
                        AudioClassifyModel.from_json(data) for data in json
                    ]
                else:
                    return AudioClassifyModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()
