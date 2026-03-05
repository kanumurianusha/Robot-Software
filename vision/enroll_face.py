import cv2
import torch
import os
from PIL import Image
from facenet_pytorch import InceptionResnetV1, MTCNN

mtcnn = MTCNN(image_size=160, margin=20)
resnet = InceptionResnetV1(pretrained='vggface2').eval()

EMBED_DIR = "embeddings"
os.makedirs(EMBED_DIR, exist_ok=True)

name = input("Enter person name: ").lower()

cap = cv2.VideoCapture(0)
samples = []

print("Look at camera. Capturing 20 samples...")

while len(samples) < 20:
    ret, frame = cap.read()
    if not ret:
        continue

    img = Image.fromarray(frame)
    face = mtcnn(img)

    if face is not None:
        emb = resnet(face.unsqueeze(0)).detach()
        samples.append(emb)
        print("Captured sample", len(samples))

    cv2.imshow("Capturing Face", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Save embeddings
torch.save(samples, f"{EMBED_DIR}/{name}.pt")
print("Saved embeddings for", name)