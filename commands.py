from gtts import gTTS
import streamlit as st
import base64
import os
import tempfile
import webbrowser

def speak(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_path = fp.name
        tts.save(temp_path)

    # Play audio in Streamlit
    with open(temp_path, "rb") as f:
        audio_data = f.read()
        b64 = base64.b64encode(audio_data).decode()
        st.audio(f"data:audio/mp3;base64,{b64}", format="audio/mp3")

def perform_action(fingers):
    if fingers == 1:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif fingers == 2:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif fingers == 3:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")
    elif fingers == 5:
        speak("Goodbye!")
