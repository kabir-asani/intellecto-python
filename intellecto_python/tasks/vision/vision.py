from os import PathLike
from ...core import *
from ..base import IntellectoBase
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
        model: str,
        path: str | PathLike[str]
    ) -> VisionClassifyModel:
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
                        VisionClassifyModel.from_json(data) for data in json
                    ]
                else:
                    return VisionClassifyModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()

    def detect(
        self,
        model: str
    ) -> VisionDetectModel:
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
                        VisionDetectModel.from_json(data) for data in json
                    ]
                else:
                    return VisionDetectModel.from_json(json)
        except IntellectoAPIStatusError as e:
            raise e
        except:
            raise IntellectoUnknownError()
