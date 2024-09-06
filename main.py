import streamlit as st
from groq import Groq
import os 
from dotenv import load_dotenv


load_dotenv()
key = os.getenv('API_KEY')
print(key)

client = Groq(api_key=key)

st.title('AI Audio Transcriber App')
audio_file = st.file_uploader('Upload an audio file',type = ['mp3', 'wav' , 'm4a'])
if audio_file :
    st.audio(audio_file)
    st.title('audio Transcript')
    trascription = client.audio.transcriptions.create(
     model= 'whisper-large-v3',
     file = audio_file ,
     prompt = 'Provide an accurate transcription of the audio file '
    )
    st.markdown(trascription.text)
