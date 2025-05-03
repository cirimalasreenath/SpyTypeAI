# utils/ollama_config.py

from langchain_community.llms import Ollama

def get_ollama_model(model_name="mistral"):
    """
    Returns an instance of the specified Ollama LLM.
    Make sure Ollama is running and the model is pulled locally.
    """
    try:
        return Ollama(model=model_name)
    except Exception as e:
        print(f"[Error] Could not load Ollama model '{model_name}': {e}")
        return None
