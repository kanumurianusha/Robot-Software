import sys
import os

# ensure project root is on sys.path when running from inside the vision directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from vision.face_detection import start_camera

if __name__ == "__main__":
    start_camera()
