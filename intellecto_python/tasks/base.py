from ..core.client import IntellectoClient, AsyncIntellectoClient


class IntellectoModel:
    pass


class IntellectoBase:
    client: IntellectoClient

    def __init__(
        self,
        token: str,
    ) -> None:
        """Construct a new synchronous intellecto base instance.
        """

        self.client = IntellectoClient(
            token=token
        )


class AsyncIntellectoBase:
    client: AsyncIntellectoClient

    def __init__(
        self,
        token: str,
    ) -> None:
        """Construct a new asynchronous intellecto base instance.
        """

        self.client = AsyncIntellectoClient(
            token=token
        )
