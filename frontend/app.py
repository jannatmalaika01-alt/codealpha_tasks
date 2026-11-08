import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/translate"

st.set_page_config(page_title="Language Translator", page_icon="🌍")
st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages.")

languages = {
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Chinese": "zh"
}

source = st.selectbox("Translate from", languages.keys())
target = st.selectbox("Translate to", languages.keys())

text = st.text_area("Enter your text", max_chars=500)

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text.")
    elif source == target:
        st.warning("Please select two different languages.")
    else:
        try:
            response = requests.post(
                API_URL,
                json={
                    "text": text,
                    "source_language": languages[source],
                    "target_language": languages[target]
                },
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            st.success("Translation successful!")
            st.text_area("Translated text", result["translated_text"])
        except requests.exceptions.RequestException as e:
            st.error(f"Translation failed: {e}")