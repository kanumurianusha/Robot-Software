# 🤖 Robot Software – Offline AI Assistant

An **offline AI-powered robot assistant** built using **Computer Vision, Speech Recognition, and Local LLMs**.
The system can recognize faces, understand voice commands, and respond using a locally running language model.

This project demonstrates integration of **AI, Machine Learning, and Robotics software architecture**.

---

# 🚀 Features

* 🎤 **Speech Recognition**

  * Uses Vosk for offline speech-to-text
  * Processes voice commands in real time

* 🧠 **AI Chat Brain**

  * Uses TinyLlama (local LLM) via llama-cpp-python
  * Generates intelligent responses offline

* 👁️ **Face Detection & Recognition**

  * Detects faces using OpenCV
  * Recognizes registered users

* 🔊 **Text to Speech**

  * Converts AI responses to voice
  * Supports gTTS / Piper TTS

* 💾 **Memory System**

  * Stores conversation context
  * Maintains robot interaction memory

---

# 🏗️ Project Architecture

```
Robot-Software
│
├── brain/                  # AI decision system
│   ├── chat_brain.py
│   ├── memory.py
│
├── vision/                 # Computer vision modules
│   ├── face_detection.py
│   ├── face_recognition_engine.py
│   ├── enroll_face.py
│
├── voice/                  # Speech recognition
│   ├── speech_to_text.py
│
├── speech/                 # Text-to-speech system
│   ├── tts.py
│
├── embeddings/             # Face embeddings
│
├── main.py                 # Main robot controller
├── config.py               # System configuration
└── requirements.txt
```

---

# 🧠 Technologies Used

* Python
* OpenCV
* Vosk Speech Recognition
* Llama.cpp
* TinyLlama LLM
* PyTorch
* Face Recognition
* MediaPipe
* Flask (optional API interface)

---

# ⚙️ Installation

Clone the repository

```
git clone https://github.com/kanumurianusha/Robot-Software.git
cd Robot-Software
```

Create virtual environment

```
python -m venv .venv
```

Activate environment

Windows

```
.venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Run the Robot Assistant

```
python main.py
```

The system will:

1. Listen to voice commands
2. Recognize the user face
3. Process the request using the AI brain
4. Respond using speech output

---

# 📦 Models (Not Included in Repo)

Large AI models are excluded from GitHub.

Download required models:

TinyLlama LLM
Vosk Speech Model

Place them inside:

```
models/
```

---

# 🧪 Testing Modules

You can test individual components:

Vision test

```
python vision/test_vision.py
```

Voice test

```
python voice/test_tts.py
```

LLM test

```
python test_llm.py
```

---

# 📌 Future Improvements

* Real-time object detection
* Emotion recognition
* Mobile robot integration
* Web dashboard interface
* Multi-language voice support

---

# 👩‍💻 Author

**Anusha Kanumuri**

Computer Science Graduate
Interested in **AI, Machine Learning, and Intelligent Systems**

GitHub:
https://github.com/kanumurianusha

---

# ⭐ Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📜 License

This project is for **educational and research purposes**.
