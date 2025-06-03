from enum import StrEnum
from typing import TypeAlias


class OpenAIModelName(StrEnum):
    GPT_4O_mini = "gpt-4o-mini"
    GPT_4O = "gpt-4o"

class AnthropicModelName(StrEnum):
    SONNET_35 = "claude-3.5-sonnet"


AllModelEnum: TypeAlias = (OpenAIModelName | AnthropicModelName)
