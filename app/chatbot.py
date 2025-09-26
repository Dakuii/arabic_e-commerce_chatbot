import ollama
import streamlit as st

st.title("Electro Chatbot")

# initialize history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Directly set the model
st.session_state["model"] = 'hf.co/Dakuiii/Electro_arabic_chatbot-Meta-Llama-3.2-3B-GGUF:latest'

def model_res_generator():
    stream = ollama.chat(
        model=st.session_state["model"],
        messages=st.session_state["messages"],
        stream=True,
    )
    for chunk in stream:
        yield chunk["message"]["content"]

# Display chat messages from history on app rerun
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    # add latest message to history in format {role, content}
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message = st.write_stream(model_res_generator())
        st.session_state["messages"].append({"role": "assistant", "content": message})
