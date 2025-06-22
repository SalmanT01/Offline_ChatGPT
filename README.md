# Offline_ChatGPT
Local voice-powered personal AI assistant using Python + Ollama

# Jarvis-LocalAI 🧠🎙️

A voice-controlled personal assistant using local LLM (LLlama3 suitable for GPU Machine and TinyLlama suitable for CPU Machine) and Python. Works offline, responds to your spoken commands, and speaks back with a voice.

## Features

- Voice recognition (speech-to-text)
- Local language model (TinyLlama via Ollama)
- Text-to-speech responses
- Continuous command loop
- Works without internet

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) (local LLM manager)
- TinyLlama model (`ollama pull tinyllama`)
- Microphone access
- Text-to-speech engine (`pyttsx3`)

## Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/Jarvis-LocalAI.git
cd Jarvis-LocalAI

# Install dependencies
pip install -r requirements.txt

