import cv2
from vision.face_recognition_engine import recognize_face


# 🔵 OLD FUNCTION (keep for testing)
def start_camera():
    print("📷 Face recognition started")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        name = recognize_face(frame)

        cv2.putText(frame, name, (30,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.imshow("Priya Vision", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# 🟢 NEW FUNCTION (robot uses this)
def scan_and_recognize_face():
    print("📷 Scanning face for greeting...")

    cap = cv2.VideoCapture(0)
    detected_name = "Unknown"

    # scan only for a short time (important!)
    for _ in range(60):   # ~2 seconds
        ret, frame = cap.read()
        if not ret:
            continue

        name = recognize_face(frame)

        cv2.putText(frame, name, (30,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.imshow("Priya Vision", frame)

        if name != "Unknown":
            detected_name = name
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    print("📷 Camera closed")
    return detected_name