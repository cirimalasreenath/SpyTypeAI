from langchain_community.llms import Ollama

class KeystrokeAnalyzer:
    def __init__(self):
        self.llm = Ollama(model="mistral")

    def analyze(self, text):
        prompt = (
            "You are a security assistant. Analyze the following keystrokes and detect:\n"
            "- Sensitive info (passwords, tokens)\n"
            "- Command-line operations\n"
            "- Suspicious or repeated patterns\n\n"
            f"Keystrokes:\n{text}\n\n"
            "Summarize your analysis:"
        )
        return self.llm.invoke(prompt)
