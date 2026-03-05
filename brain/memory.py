from rapidfuzz import fuzz

MEMORY_FILE = "brain/robot_memory.txt"

memory_db = {}

# ---------------- LOAD MEMORY ----------------
def load_memory():
    global memory_db
    memory_db = {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                question, answer = line.split("=", 1)
                memory_db[question.strip().lower()] = answer.strip()

load_memory()

# ---------------- SMART MATCH ----------------
def check_memory(user_text):
    user_text = user_text.lower().strip()

    best_score = 0
    best_answer = None

    for question, answer in memory_db.items():
        score = fuzz.partial_ratio(user_text, question)

        if score > best_score:
            best_score = score
            best_answer = answer

    # 🔥 threshold controls strictness
    if best_score > 80:
        print("🧠 Memory matched with score:", best_score)
        return best_answer

    return None