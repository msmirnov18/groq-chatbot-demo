import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

if "messages" not in st.session_state:
    st.session_state.messages = []


# Initialize audio counter
if "audio_count" not in st.session_state:
    st.session_state.audio_count = 0


# Audio input with dynamic key
if audio := st.audio_input("Record a voice message", key=f"audio_{st.session_state.audio_count}"):

    # Transcribe with Wisper
    transcription = client.audio.transcriptions.create(
        model = "whisper-large-v3",
        file=("audio.wav", audio.read()),
    )

    prompt = transcription.text
    
    # Display user message
    st.write(f"You said: {prompt}")

    # Add to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    # Extract assistant reply
    reply = response.choices[0].message.content

    # Add to history and display
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

    # Increment counter to reset widget
    st.session_state.audio_count += 1
    st.rerun()


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Text input
if prompt := st.chat_input("Say something"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Call Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )
    
    # Extract assistant reply
    reply = response.choices[0].message.content
    
    # Add to history and display
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)