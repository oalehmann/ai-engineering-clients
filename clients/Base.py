from abc import ABC, abstractmethod
from typing import AsyncIterator

from schemas import ChatMessage, ModelResponse


class BaseLLMClient(ABC):

    @abstractmethod
    async def generate(
        self,
        messages: list[ChatMessage]
    ) -> ModelResponse:
        pass

    @abstractmethod
    async def generate_stream(
        self,
        messages: list[ChatMessage]
    ) -> AsyncIterator[str]:
        pass
