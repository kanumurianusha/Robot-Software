from llama_cpp import Llama

model = Llama(
    model_path="models/llm/TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf",
    n_ctx=1024,
    n_threads=4
)

output = model(
    "User: What is artificial intelligence?\nAssistant:",
    max_tokens=100
)

print(output["choices"][0]["text"])