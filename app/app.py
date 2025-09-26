import streamlit as st
import ollama

# Initialize Streamlit app
st.title('Arabic E-Commerce Chatbot')
st.write('Ask me anything!')

# Initialize session state to store chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Get user input
user_input = st.text_input('Your question:', '')

# Process the input when the user submits
if user_input:
    # Add user input to chat history
    st.session_state.messages.append({'role': 'user', 'content': user_input})

    # Call Ollama model with the chat history
    response = ollama.chat(
        model='hf.co/Dakuiii/Electro_arabic_chatbot-Meta-Llama-3.2-3B-GGUF:latest',
        messages=st.session_state.messages,
        stream=False
    )
    
    # Add assistant's response to chat history
    st.session_state.messages.append({'role': 'assistant', 'content': response.message.content})

# Display the chat history
st.write("Chat History:")
for message in st.session_state.messages:
    if message['role'] == 'user':
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Bot:** {message['content']}")

