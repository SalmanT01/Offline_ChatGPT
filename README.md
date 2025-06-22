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
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Install and run Ollama

Download and install Ollama from https://ollama.com/download
tinyllama (If no GPU)
llama3 (GPU Required)
more LLM models options also available. Need to Edit the script

Open terminal and run:
```bash
ollama pull tinyllama 
ollama pull llama3 
```

## Running the Assistant
```bash
python jarvis2.0.py
```

## Project Structure
```bash
Jarvis-LocalAI/
├── jarvis2.0.py           # Main script
├── requirements.txt       # Python dependencies
├── README.md              # Project info
├── assets/                # Optional audio/logo/images
└── .gitignore             # Python cache & env ignores
```
