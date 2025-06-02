from agents import ChatBot
from memory import PostgresMemory
from core import settings

from langchain_core.messages import HumanMessage


if __name__ == "__main__":
    
    # build graph
    chatbot = ChatBot()
    builder = chatbot.graph_builder()

    # setup memory
    memory = PostgresMemory(settings.DATABASE_URL)
    memory.setup()

    # compile
    graph = builder.compile(
        checkpointer=memory.get_checkpointer()
    )

    user_input = input("Enter a message: ")
    while user_input != "q":
        config = {
            "configurable": {
                "thread_id": "1",
                "user_id": "1"
            }
        }
        response = graph.invoke({
            "messages": [HumanMessage(content=user_input)]
        }, config)

        response = response["messages"][-1].content
        print(response)
        user_input = input("Enter a message: ")
