
class IntellectoError(BaseException):
    pass


class IntellectoMissingAccessTokenError(IntellectoError):
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
