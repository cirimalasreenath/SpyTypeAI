# SpyTypeAI

SpyTypeAI is a GUI-based keylogger with AI-based analysis using local LLMs (Mistral via Ollama). It captures and evaluates user keystrokes for suspicious or sensitive patterns.

## Features
- Tkinter GUI
- Admin login for access control
- Real-time keystroke logging
- LLM (Mistral) analysis via Ollama
- Modular architecture

## Setup
```bash
pip install -r requirements.txt
ollama run mistral
python main.py
