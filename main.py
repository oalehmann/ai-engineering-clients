import asyncio
import os

from schemas import ChatMessage, LLMConfig, Provider
from clients.openai_client import OpenAIClient
from clients.anthropic_client import AnthropicClient


async def main():

    proveedor = os.environ.get("LLM_PROVIDER", "openai").lower()

    if proveedor == "openai":
        api_key = os.environ.get("OPENAI_API_KEY")
        provider = Provider.OPENAI
        modelo = "gpt-4o-mini"
        ClienteLLM = OpenAIClient

    elif proveedor == "anthropic":
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        provider = Provider.ANTHROPIC
        modelo = "claude-3-5-haiku-latest"
        ClienteLLM = AnthropicClient

    else:
        raise ValueError(
            "LLM_PROVIDER debe ser 'openai' o 'anthropic'."
        )

    if not api_key:
        raise RuntimeError(
            f"Falta configurar la clave de API para {proveedor}."
        )

    config = LLMConfig(
        provider=provider,
        model=modelo,
        temperature=0.2,
        max_tokens=200
    )

    cliente = ClienteLLM(
        config=config,
        api_key=api_key
    )

    mensajes = [
        ChatMessage(
            role="user",
            content="Explicá brevemente qué es un LLM."
        )
    ]

    respuesta = await cliente.generate(mensajes)

    print("\nRespuesta del modelo:")
    print(respuesta.content)

    print("\nRespuesta en streaming:")

    async for fragmento in cliente.generate_stream(mensajes):
        print(fragmento, end="", flush=True)

    print()


if __name__ == "__main__":
    asyncio.run(main())
