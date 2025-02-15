from llama_cpp import Llama

class LlamaChat:
    def __init__(self, model_path):
        self.llm = Llama(model_path=model_path, verbose=False, n_ctx=2048, n_threads=4)
        self.conversation_history = ""

    def generateResponse(self, userInput):
        formatted_prompt = f"""You are a helpful AI assistant.
        You will have a conversation with the user and answer their questions in a helpful manner.

        ### Conversation History ###
        {self.conversation_history}

        ### User: {userInput}
        ### AI:"""

        output = self.llm.create_completion(prompt=formatted_prompt, max_tokens=200, stop=["\n"])
        response = output["choices"][0]["text"].strip()

        self.conversation_history += f"\nUser: {userInput}\nAI: {response}"  # Persist history

        return response
