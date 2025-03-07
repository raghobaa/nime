import streamlit as st
import conver
from conver import URLToAudioConverter
from dataclasses import dataclass

st.set_page_config(
    page_title="NarrateLink",
    page_icon="🔊",
    layout="wide",
    initial_sidebar_state="expanded",
)

@dataclass
class ConversationConfig:
    max_words: int = 15000
    prefix_url: str = "https://r.jina.ai/"
    model_name: str = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

if "audio_file" not in st.session_state:
    st.session_state.audio_file = None

with st.sidebar:
    st.image("https://img.icons8.com/clouds/100/000000/podcast.png", width=100)
    st.title("Settings")
    
    st.subheader("🎤 Voice Settings")
    voices_dict = {
        "Asteria (English - US, Female)": "aura-asteria-en",
        "Luna (English - US, Female)": "aura-luna-en",
        "Stella (English - US, Female)": "aura-stella-en",
        "Athena (English - UK, Female)": "aura-athena-en",
        "Hera (English - US, Female)": "aura-hera-en",
        "Orion (English - US, Male)": "aura-orion-en",
        "Arcas (English - US, Male)": "aura-arcas-en",
        "Perseus (English - US, Male)": "aura-perseus-en",
        "Angus (English - Ireland, Male)": "aura-angus-en",
        "Orpheus (English - US, Male)": "aura-orpheus-en",
        "Helios (English - UK, Male)": "aura-helios-en",
        "Zeus (English - US, Male)": "aura-zeus-en",
    }

    voices = list(voices_dict.keys())

    voice_1 = st.selectbox("Speaker 1", voices, index=7)
    voice_2 = st.selectbox("Speaker 2", voices, index=0)

st.title("🎧 NarrateLink")
st.caption("Transform articles into engaging podcasts instantly")

# Replacing user input with a fixed website link
st.markdown("### Source Website")
st.markdown("[Visit AQI](https://www.aqi.in/us)", unsafe_allow_html=True)

st.divider()
st.markdown(
    """
    <div style='text-align: center'>
        <p>Want a secure, private text-to-speech solution? Check out 
        <a href='https://huggingface.co/spaces/eswardivi/Podcastify'>Podcastify</a> 
        </p>
        the open-source alternative that runs entirely on your device.
    </div>
    """,
    unsafe_allow_html=True,
)
