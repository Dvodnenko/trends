import ollama


class LLMClient:
    def __init__(self, model: str = "mistral"):
        self.model = model

    def ask(self, prompt: str) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.message.content
