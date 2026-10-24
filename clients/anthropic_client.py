
from anthropic import AsyncAnthropic
from typing import AsyncIterator

from schemas import ChatMessage, ModelResponse, LLMConfig, Provider
from clients.base import BaseLLMClient


class AnthropicClient(BaseLLMClient):

    def __init__(self, config: LLMConfig, api_key: str):
        self.config = config
        self.client = AsyncAnthropic(api_key=api_key)

    async def generate(
        self,
        messages: list[ChatMessage]
    ) -> ModelResponse:

        # Anthropic recibe los mensajes en un formato similar,
        # pero el system prompt se envía por separado.
        system_messages = [
            mensaje.content
            for mensaje in messages
            if mensaje.role == "system"
        ]

        user_messages = [
            {"role": mensaje.role, "content": mensaje.content}
            for mensaje in messages
            if mensaje.role != "system"
        ]

        response = await self.client.messages.create(
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            system="\n".join(system_messages),
            messages=user_messages
        )

        texto = "".join(
            bloque.text
            for bloque in response.content
            if bloque.type == "text"
        )

        return ModelResponse(
            content=texto,
            model=response.model,
            provider=Provider.ANTHROPIC
        )

    async def generate_stream(
        self,
        messages: list[ChatMessage]
    ) -> AsyncIterator[str]:

        system_messages = [
            mensaje.content
            for mensaje in messages
            if mensaje.role == "system"
        ]

        user_messages = [
            {"role": mensaje.role, "content": mensaje.content}
            for mensaje in messages
            if mensaje.role != "system"
        ]

        async with self.client.messages.stream(
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            system="\n".join(system_messages),
            messages=user_messages
        ) as stream:

            async for texto in stream.text_stream:
                yield texto
