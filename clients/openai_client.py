from openai import AsyncOpenAI
from typing import AsyncIterator

from schemas import ChatMessage, ModelResponse, LLMConfig, Provider
from clients.base import BaseLLMClient


class OpenAIClient(BaseLLMClient):

    def __init__(self, config: LLMConfig, api_key: str):
        self.config = config
        self.client = AsyncOpenAI(api_key=api_key)

    async def generate(
        self,
        messages: list[ChatMessage]
    ) -> ModelResponse:

        response = await self.client.chat.completions.create(
            model=self.config.model,
            messages=[
                {"role": mensaje.role, "content": mensaje.content}
                for mensaje in messages
            ],
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens
        )

        return ModelResponse(
            content=response.choices[0].message.content or "",
            model=response.model,
            provider=Provider.OPENAI
        )

    async def generate_stream(
        self,
        messages: list[ChatMessage]
    ) -> AsyncIterator[str]:

        stream = await self.client.chat.completions.create(
            model=self.config.model,
            messages=[
                {"role": mensaje.role, "content": mensaje.content}
                for mensaje in messages
            ],
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens,
            stream=True
        )

        async for chunk in stream:
            texto = chunk.choices[0].delta.content

            if texto:
                yield texto
