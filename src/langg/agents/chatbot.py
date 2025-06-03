from langgraph.graph import START, END, StateGraph
from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages

from langg.core import get_llm, settings


class State(TypedDict):
    messages: Annotated[list, add_messages]


class ChatBot:
    def __init__(self):
        """
        
        """
        self.model = get_llm(settings.DEFAULT_MODEL)

    def graph_builder(self):
        """
        
        """
        builder = StateGraph(State)

        builder.add_node("chatbot", self.chat)
        builder.add_edge(START, "chatbot")
        builder.add_edge("chatbot", END)

        return builder

    def chat(self, state: State) -> State:
        """
        
        """
        response = self.model.invoke(state["messages"])
        return {
            "messages": [response]
        }


if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot()
