import time
import os

from voice.speech_to_text import listen
from brain.chat_brain import generate_reply
from vision.face_detection import scan_and_recognize_face
from gtts import gTTS
from playsound import playsound

# ---------------- GLOBAL STATE ----------------
ROBOT_STATE = "SLEEP"
SLEEP_TIMEOUT = 25

WAKE_WORD = "yeah"
last_wake_time = 0
WAKE_COOLDOWN = 3


# ---------------- SPEAK ----------------
def speak(text):
    print("Priya:", text)
    tts = gTTS(text=text, lang='en')
    tts.save("reply.mp3")
    playsound("reply.mp3")
    os.remove("reply.mp3")


# ---------------- WAKE WORD DETECTION ----------------
def wake_word_detected(text):
    global last_wake_time

    text = text.lower().strip()

    # cooldown protection
    if time.time() - last_wake_time < WAKE_COOLDOWN:
        return False

    triggers = ["yeah", "yeah priya", "yeah robot", "yeah hello"]

    for phrase in triggers:
        if text.startswith(phrase):
            last_wake_time = time.time()
            return True

    if text == "yeah":
        last_wake_time = time.time()
        return True

    return False


# ---------------- FACE GREETING ----------------
def greet_user_after_wake():
    speak("Let me see who is in front of me.")

    name = scan_and_recognize_face()

    if name != "Unknown":
        speak(f"Hello {name}, nice to see you.")
    else:
        speak("Hello, I don't think we have met yet.")

    speak("How can I help you?")


# ---------------- CONVERSATION MODE ----------------
def conversation_mode():
    global ROBOT_STATE

    last_interaction = time.time()
    speak("I am listening.")

    while ROBOT_STATE == "CHAT":
        print("🟢 Listening (chat mode)...")
        command = listen()
        print("User:", command)

        # silence timeout → go back to sleep
        if command.strip() == "":
            if time.time() - last_interaction > SLEEP_TIMEOUT:
                speak("Going back to sleep.")
                ROBOT_STATE = "SLEEP"
                break
            continue

        last_interaction = time.time()

        # manual exit
        if "bye" in command or "sleep" in command or "stop" in command:
            speak("Going back to sleep.")
            ROBOT_STATE = "SLEEP"
            break

        reply = generate_reply(command)
        speak(reply)


# ---------------- MAIN LOOP ----------------
def main_loop():
    global ROBOT_STATE

    print("🤖 Robot started")
    print("Say 'yeah' to wake me")

    while True:

        # ---------- SLEEP MODE ----------
        if ROBOT_STATE == "SLEEP":
            print("😴 Waiting for wake word...")
            text = listen()
            print("Heard:", text)

            if wake_word_detected(text):
                speak("Yes?")
                greet_user_after_wake()
                ROBOT_STATE = "CHAT"
                conversation_mode()


if __name__ == "__main__":
    main_loop()