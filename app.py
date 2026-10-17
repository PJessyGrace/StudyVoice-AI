import base64
import os
import streamlit as st
from dotenv import load_dotenv
from sarvamai import SarvamAI
from sarvamai.core.api_error import ApiError

load_dotenv()

st.set_page_config(page_title="StudyVoice AI", page_icon="🎧", layout="centered")
st.title("🎧 StudyVoice AI")
st.write("Turn your study notes into spoken audio in English, Telugu, or Hindi.")

api_key = os.getenv("SARVAM_API_KEY")

if not api_key:
    st.error("API key not found. Add SARVAM_API_KEY to your local .env file, then restart the app.")
    st.code("SARVAM_API_KEY=your_real_key_here", language="text")
    st.stop()

language_options = {
    "English (India)": "en-IN",
    "Telugu": "te-IN",
    "Hindi": "hi-IN",
}

language_label = st.selectbox("Audio language", list(language_options.keys()))
study_text = st.text_area(
    "Paste your study notes",
    value="An ECG is a test that records the electrical activity of the heart. Small sensors placed on the skin detect these signals and display them as a waveform.",
    height=180,
    max_chars=2500,
    help="Keep your text under 2,500 characters for this demo."
)

if st.button("Generate audio", type="primary", use_container_width=True):
    if not study_text.strip():
        st.warning("Please enter some text first.")
    else:
        try:
            with st.spinner("Calling the text-to-speech API..."):
                client = SarvamAI(api_subscription_key=api_key)
                response = client.text_to_speech.convert(
                    text=study_text.strip(),
                    language_code=language_options[language_label],
                    model="bulbul:v3",
                )

                audio_b64 = "".join(response.audios)
                audio_bytes = base64.b64decode(audio_b64)

            st.success("Audio generated successfully!")
            st.audio(audio_bytes, format="audio/wav")
            st.download_button(
                "Download audio",
                data=audio_bytes,
                file_name="studyvoice_notes.wav",
                mime="audio/wav",
                use_container_width=True,
            )
        except ApiError as exc:
            st.error(f"The API returned an error (HTTP {exc.status_code}). Check your API key, quota, language, and request.")
            st.caption("Do not share your API key in screenshots or public issue reports.")
        except Exception as exc:
            st.error("Something went wrong while generating audio.")
            st.write(f"Error type: {type(exc).__name__}")
            st.caption("Check that the packages are installed and that your API key is valid.")
