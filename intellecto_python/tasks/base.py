from ..core import *


class IntellectoModel:
    pass


class IntellectoBase:
    token: str

    def __init__(
        self,
        token: str,
    ) -> None:
        """Construct a new synchronous intellecto base instance.
        """
        self.token = token

    def client(self) -> IntellectoClient:
        client = IntellectoClient(
            base_url="https://api-inference.huggingface.co/models",
            token=self.token
        )

        return client

    def raise_error(status_code: int):
        match status_code:
            case 400:
                raise IntellectoBadRequestError()
            case 401:
                raise IntellectoAuthenticationError()
            case 403:
                raise IntellectoPermissionDeniedError()
            case 404:
                raise IntellectoNotFoundError()
            case 422:
                raise IntellectoUnprocessableEntityError()
            case 429:
                raise IntellectoRateLimitError()
            case _:
                raise IntellectoInternalServerError()


class AsyncIntellectoBase:
    token: str

    def __init__(
        self,
        token: str,
    ) -> None:
        """Construct a new asynchronous intellecto base instance.
        """
        self.token = token

    @property
    def client(self) -> IntellectoClient:
        with IntellectoClient(
            base_url="https://api-inference.huggingface.co/models",
            token=self.token
        ) as client:
            return client

    def raise_error_based_on(status_code: int):
        match status_code:
            case 400:
                raise IntellectoBadRequestError()
            case 401:
                raise IntellectoAuthenticationError()
            case 403:
                raise IntellectoPermissionDeniedError()
            case 404:
                raise IntellectoNotFoundError()
            case 422:
                raise IntellectoUnprocessableEntityError()
            case 429:
                raise IntellectoRateLimitError()
            case _:
                raise IntellectoInternalServerError()
