import streamlit as st
from agents import ChatBot
from memory import PostgresMemory
from core import settings
from langchain_core.messages import HumanMessage


# Set up chatbot and memory (initialize once and cache in session state)
if "chatbot" not in st.session_state:
    chatbot = ChatBot()
    builder = chatbot.graph_builder()
    memory = PostgresMemory(settings.DATABASE_URL)
    memory.setup()
    graph = builder.compile(checkpointer=memory.get_checkpointer())
    st.session_state.chatbot = chatbot
    st.session_state.graph = graph
else:
    graph = st.session_state.graph


# Show title and description.
st.title("💬 Chatbot")

with st.sidebar:
    st.title("💬 AI Agent")
    st.write("Let's chat!")

# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.chat_input("What is up?"):

    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Run the agent graph as in run_agent.py
    config = {
        "configurable": {
            "thread_id": "1",
            "user_id": "1"
        }
    }
    response = graph.invoke({
        "messages": [HumanMessage(content=prompt)]
    }, config)
    last_content = response["messages"][-1].content

    # Store and display the assistant's response.
    st.session_state.messages.append({"role": "assistant", "content": last_content})
    with st.chat_message("assistant"):
        st.markdown(last_content)
