from gtts import gTTS
import tempfile
import base64
import streamlit as st

def speak_text(text):
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
        tts.save(fp.name)
        audio_file = fp.read()
        b64 = base64.b64encode(audio_file).decode()
        st.audio(fp.name, format='audio/mp3')

def perform_action(fingers):
    if fingers == 1:
        text = "Opening Google"
        url = "https://www.google.com"
    elif fingers == 2:
        text = "Opening GitHub"
        url = "https://www.github.com"
    elif fingers == 3:
        text = "Opening YouTube"
        url = "https://www.youtube.com"
    elif fingers == 5:
        text = "Goodbye!"
        url = None
    else:
        text = "Gesture not recognized"
        url = None

    speak_text(text)

    if url:
        st.markdown(f"🔗 [Click here to open {url}]({url})", unsafe_allow_html=True)
