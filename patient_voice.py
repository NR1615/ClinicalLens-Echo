import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def record_audio(file_path, timeout=20, phrase_time_limit=None):
    recognizer = sr.Recognizer()
    audio_data = None

    try:
        with sr.Microphone() as source:
            logging.info("adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("start speaking now")
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Audio recording complete.")

            wav_data=audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")

            logging.info("Audio converted to MP3 format and saved to {file_path}.")
    except Exception as e:
        logging.error(f"Error recording audio: {e}")

    return audio_data

#audio_file_path = "audio/patient_voice.mp3"
#record_audio(file_path=audio_file_path)

model="whisper-large-v3-turbo"
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY not found in .env")

def transcribe_with_groq(model, audio_file_path, api_key):
    audio_file=open(audio_file_path,"rb")
    client=Groq(api_key=api_key)
    model="whisper-large-v3-turbo"
    transcription = client.audio.transcriptions.create(
        model=model,
        file=audio_file,
        temperature=0,
        language="en"
    )
    return transcription.text
