import os
from gtts import gTTS
import elevenlabs
import subprocess
import platform
from dotenv import load_dotenv
load_dotenv()



def text_to_speech_old(input_text, output_filepath):
    language = 'en'
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)


#input_text = "Hello, I have reviewed your symptoms and the image you provided"
#text_to_speech_old(input_text, "audio/doctor_voice.mp3")


ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
if not ELEVENLABS_API_KEY:
    raise RuntimeError("ELEVENLABS_API_KEY not found in .env")

def text_to_speech_ellabs_old(input_text, output_filepath):
    client = elevenlabs.ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="UgBBYS2sOqTuMpoF3BR0",
        model_id="eleven_multilingual_v2"
        
    )
    elevenlabs.save(audio, output_filepath)

#input_text_ellabs = "Hello, I have reviewed your symptoms and the image you provided using Eleven Labs"
#text_to_speech_ellabs_old(input_text_ellabs, "audio/doctor_voice_ellabs.mp3")


def text_to_speech(input_text, output_filepath):
    language = 'en'
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)
    os_name=platform.system()
    try:
        if os_name=="Darwin":
            subprocess.call(["afplay",output_filepath])
        elif os_name=="Windows":
            subprocess.run(['powerhell',"-c",f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name=="Linux":
            subprocess.call(["aplay",output_filepath])
        else:
            raise OSError("Unsupported OS for audio playback")
    except Exception as e:
        print(f"Error playing audio: {e}")
    


#input_text = "Hello, I have reviewed your symptoms and the image you provided autoplay"
#text_to_speech(input_text, "audio/doctor_voice_autoplay.mp3")


def text_to_speech_ellabs(input_text, output_filepath):
    client = elevenlabs.ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="UgBBYS2sOqTuMpoF3BR0",
        model_id="eleven_multilingual_v2"
        
    )
    elevenlabs.save(audio, output_filepath)
    os_name=platform.system()
    try:
        if os_name=="Darwin":
            subprocess.call(["afplay",output_filepath])
        elif os_name=="Windows":
            subprocess.run(['powerhell',"-c",f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name=="Linux":
            subprocess.call(["aplay",output_filepath])
        else:
            raise OSError("Unsupported OS for audio playback")
    except Exception as e:
        print(f"Error playing audio: {e}")

#input_text_ellabs = "Hello, I have reviewed your symptoms and the image you provided using Eleven Labs autoplay"
#text_to_speech_ellabs(input_text_ellabs, "audio/doctor_voice_ellabs_autoplay.mp3")