# 🩺 ClinicalLens-Echo

**ClinicalLens-Echo** is an AI-powered clinical assistant that simulates doctor–patient interactions using **speech recognition**, **text-to-speech**, and **multimodal AI reasoning**.  
It supports patient voice input, doctor voice output, and optional image-based clinical analysis.

---

## ✨ Features

- 🎤 **Patient Voice Input**
  - Records patient speech
  - Transcribes audio using AI speech recognition
- 🧑‍⚕️ **Doctor Voice Output**
  - Converts AI-generated responses into natural speech
- 🧠 **AI Reasoning Core**
  - Processes text, audio, and images
  - Generates medical-style responses
- 🖼️ **Image Understanding**
  - Encodes and analyzes images for multimodal reasoning
- 🌐 **Extensible Architecture**
  - Easy to integrate with Gradio or other web frameworks

---

## 📂 Project Structure

```
ClinicalLens-Echo/
│
├── brain.py
├── patient_voice.py
├── doctor_voice.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Requirements

- Python **3.9+**
- Working microphone
- API keys for supported AI services

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

---

## 🚀 Usage

```bash
python patient_voice.py
python brain.py
python doctor_voice.py
```

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only** and does **not** provide medical advice.

---

## 📄 License

MIT License
