from ..core.client import IntellectoClient, AsyncIntellectoClient


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


class IntellectoError:
    pass


class IntellectoAPIConnectionError(IntellectoError):
    pass


class IntellectoUnknownError(IntellectoError):
    pass


class IntellectoAPIStatusError(IntellectoError):
    status_code: int

    def __init__(
        self,
        status_code: int
    ) -> None:
        self.status_code = status_code


class IntellectoBadRequestError(IntellectoAPIStatusError):
    def __init__(
        self
    ) -> None:
        super().__init__(status_code=400)


class IntellectoAuthenticationError(IntellectoAPIStatusError):
    def __init__(
        self
    ) -> None:
        super().__init__(status_code=401)


class IntellectoPermissionDeniedError(IntellectoAPIStatusError):
    def __init__(
        self
    ) -> None:
        super().__init__(status_code=403)


class IntellectoNotFoundError(IntellectoAPIStatusError):
    def __init__(
        self
    ) -> None:
        super().__init__(status_code=404)


class IntellectoUnprocessableEntityError(IntellectoAPIStatusError):
    def __init__(
        self
    ) -> None:
        super().__init__(status_code=422)


class IntellectoRateLimitError(IntellectoAPIStatusError):
    def __init__(
        self
    ) -> None:
        super().__init__(status_code=429)


class IntellectoInternalServerError(IntellectoAPIStatusError):
    def __init__(
        self,
        status_code: int
    ) -> None:
        super().__init__(status_code=status_code)
