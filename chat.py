from llama_cpp import Llama

# Store conversation history
conversation_history = ""

def loadModel():
# Load the model
    llm = Llama(
        model_path="/Users/shiraz/Documents/LLMs/llama.cpp/models/deepseek-llm-7b-chat.Q4_K_M.gguf",
        verbose=False,
        n_ctx=2048,
        n_threads=4
    )

# while True:
    # user_input = input("You: ")  # Get user input
    # if user_input.lower() in ["exit", "quit"]:
    #     break  # Exit the chat

    # Format the interactive prompt

def generateResponse(userInput):
    formatted_prompt = f"""You are a helpful AI assistant.
    You will have a conversation with the user and answer their questions in a helpful manner.

    ### Conversation History ###
    {conversation_history}

    ### User: {userInput}
    ### AI:"""

    # Generate response
    output = llm.create_completion(prompt=formatted_prompt, max_tokens=200, stop=["\n"])
    response = output["choices"][0]["text"].strip()

    # print("AI:", response)

    # Update conversation history
    conversation_history += f"\nUser: {userInput}\nAI: {response}"

    return response 
