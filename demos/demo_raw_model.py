from llama_cpp import Llama

# Load the model from a Hugging Face repo
# llm = Llama.from_pretrained(
#     repo_id="QuantFactory/Dolphin3.0-Llama3.2-1B-GGUF",
#     filename="Dolphin3.0-Llama3.2-1B.Q2_K.gguf",
# )
llm = Llama.from_pretrained(
    repo_id="unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
    filename="DeepSeek-R1-Distill-Qwen-1.5B-Q2_K.gguf",
)

# Define conversation messages in chat format
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]

# Generate response
response = llm.create_chat_completion(messages=messages)

# Print the model's reply
print(response["choices"][0]["message"]["content"])
