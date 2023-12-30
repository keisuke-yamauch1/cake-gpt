import os


class OpenAIInfo:
    def __init__(self, model_name=None, temperature=None):
        self.model_name = model_name if model_name else os.environ["OPENAI_API_MODEL"]
        self.temperature = temperature if temperature else os.environ["OPENAI_API_TEMPERATURE"]
        self.api_key = os.environ["OPENAI_API_KEY"]
