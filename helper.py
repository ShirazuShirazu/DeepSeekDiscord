from LlamaChat import LlamaChat

llmModel = LlamaChat("/Users/shiraz/Documents/LLMs/llama.cpp/models/deepseek-llm-7b-chat.Q4_K_M.gguf")

def generate_response(message):
    return llmModel.generateResponse(message)
