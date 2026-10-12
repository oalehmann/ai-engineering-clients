
from enum import Enum
from pydantic import BaseModel, Field


class Provider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"


class ChatMessage(BaseModel):
    role: str
    content: str


class LLMConfig(BaseModel):
    provider: Provider
    model: str
    temperature: float = Field(default=0.7, ge=0, le=2)
    max_tokens: int = 1024


class ModelResponse(BaseModel):
    content: str
    model: str
    provider: Provider
