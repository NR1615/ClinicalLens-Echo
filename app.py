import gradio as gr
from brain import encode_image_to_base64, analyze_image_with_query
from patient_voice import record_audio, transcribe_with_groq
from doctor_voice import text_to_speech_ellabs, text_to_speech
from dotenv import load_dotenv
load_dotenv()
import os
import anthropic
import groq

system_prompt="""You have to act as a professional doctor, I know you are not but this is for learning purpose. what's in this image?. Do you find anything wrong with it medically? If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person. Donot say 'In the image I see' but say 'With what I see, I think you have ....' Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, Keep your answer concise (max 2 sentences). No preamble, start your answer right away please
"""

def process_inputs(audio_filepath, image_filepath):
    # Transcribe patient audio
    transcription_text = transcribe_with_groq(
        model="whisper-large-v3-turbo",
        audio_file_path=audio_filepath,
        api_key=os.getenv("GROQ_API_KEY")
    )

    if image_filepath:  # Encode image to base64
        image_base64, media_type = encode_image_to_base64(image_filepath)

        doctor_response = analyze_image_with_query(
            Query=f"{system_prompt}\n\nPatient said: {transcription_text}", image_base64=image_base64,
            media_type=media_type)

    else:
        doctor_response = "No image provided for analysis."
    # Convert doctor's response to speech

    doctor_voice=text_to_speech(doctor_response, "audio/doctor_response.mp3")   

    return transcription_text, doctor_response, doctor_voice




iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath",),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="temp.mp3")
    ],
    title="ClinicalLens-Echo",
)

iface.launch(debug=True)

