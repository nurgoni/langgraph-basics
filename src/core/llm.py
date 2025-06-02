from functools import cache
from typing import TypeAlias

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from schemas.models import (
    AllModelEnum, 
    AnthropicModelName, 
    OpenAIModelName
)

from core import settings


ModelOutput: TypeAlias = (ChatOpenAI | ChatAnthropic)


@cache
def get_llm(model_name: AllModelEnum) -> ModelOutput:
    if model_name in OpenAIModelName:
        return ChatOpenAI(
            model_name=model_name,
            openai_api_key=settings.OPENAI_API_KEY,
            temperature=0,
            streaming=True
        )
    elif model_name in AnthropicModelName:
        return ChatAnthropic(model_name=model_name)
    else:
        raise ValueError(f"Invalid model name: {model_name}")