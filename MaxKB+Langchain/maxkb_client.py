from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class MaxKBConfig:
    base_url: str
    api_key: str
    timeout: int = 60


class MaxKBClient:
    def __init__(self, config: MaxKBConfig):
        self.config = config
        self.chat_id: str | None = None

    def build_url(self, path: str) -> str:
        base_url = self.config.base_url.rstrip("/")
        path = path.lstrip("/")
        return f"{base_url}/{path}"

    def build_headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json",
        }

    def open_chat(self) -> str:
        response = requests.get(
            self.build_url("open"),
            headers=self.build_headers(),
            timeout=self.config.timeout,
        )
        response.raise_for_status()

        response_data = response.json()
        if response_data.get("code") != 200:
            raise RuntimeError(response_data)

        self.chat_id = response_data["data"]
        return self.chat_id

    def ask(self, question: str) -> dict[str, Any]:
        if self.chat_id is None:
            self.open_chat()

        payload = {
            "message": question,
            "stream": False,
            "re_chat": False,
        }

        response = requests.post(
            self.build_url(f"chat_message/{self.chat_id}"),
            headers=self.build_headers(),
            json=payload,
            timeout=self.config.timeout,
        )
        response.raise_for_status()

        response_data = response.json()
        if response_data.get("code") != 200:
            raise RuntimeError(response_data)

        return response_data


if __name__ == "__main__":
    config = MaxKBConfig(
        base_url="http://localhost:8080/chat/api",
        api_key="agent-e7548373280006f8b5b48ca5f70361e6",
    )

    client = MaxKBClient(config)
    result = client.ask("手机整机保修多久？")
    print(result["code"])
    print(result["data"]["content"])
