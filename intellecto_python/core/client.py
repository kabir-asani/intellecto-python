from httpx import Client, AsyncClient


class IntellectoClient(Client):
    def __init__(
        self,
        token: str,
        base_url: str
    ) -> None:
        super().__init__(
            base_url=base_url,
            headers={
                'Authorization': f'Bearer {token}'
            }
        )


class AsyncIntellectoClient(AsyncClient):
    def __init__(
        self,
        token: str,
        base_url: str
    ) -> None:
        super().__init__(
            base_url=base_url,
            headers={
                'Authorization': f'Bearer {token}'
            }
        )
