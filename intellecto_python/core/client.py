from httpx import Client, AsyncClient


class IntellectoClient(Client):
    def __init__(
        self,
        token: str
    ) -> None:
        super().__init__(
            base_url="https://api-inference.huggingface.co/models",
            headers={
                'Authorization': f'Bearer {token}'
            }
        )


class AsyncIntellectoClient(AsyncClient):
    def __init__(
        self,
        token: str
    ) -> None:
        super().__init__(
            base_url="https://api-inference.huggingface.co/models",
            headers={
                'Authorization': f'Bearer {token}'
            }
        )
