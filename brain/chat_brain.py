from llama_cpp import Llama
from brain.memory import check_memory

print("🧠 Loading TinyLlama brain...")

MODEL_PATH = "models/llm/TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=512,
    n_threads=4,
    n_batch=256,
    use_mmap=True,
    use_mlock=False,
    verbose=False
)

print("🧠 Brain ready!")


def generate_reply(prompt):
    user_text = prompt.lower().strip()

    # 🔎 Memory first
    memory_answer = check_memory(user_text)
    if memory_answer:
        return memory_answer

    # 🟢 LLM fallback
    full_prompt = f"""You are Priya, a friendly home robot.
Speak short and clearly.

User: {user_text}
Priya:"""

    output = llm(
        full_prompt,
        max_tokens=80,
        temperature=0.6,
        top_p=0.9,
        repeat_penalty=1.1,
        stop=["User:", "Priya:"]
    )

    reply = output["choices"][0]["text"].strip()

    if reply == "":
        reply = "I didn't understand. Can you repeat?"

    return reply