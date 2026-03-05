import os
import torch
from PIL import Image
from facenet_pytorch import InceptionResnetV1, MTCNN

mtcnn = MTCNN(image_size=160, margin=20)
resnet = InceptionResnetV1(pretrained='vggface2').eval()

EMBED_DIR = "embeddings"
known_embeddings = {}
print("🔵 Loading trained faces...")

for file in os.listdir(EMBED_DIR):
    if file.endswith(".pt"):
        name = file.split(".")[0]
        known_embeddings[name] = torch.load(f"{EMBED_DIR}/{file}")
        print("Loaded:", name)


def recognize_face(frame):
    img = Image.fromarray(frame)
    face = mtcnn(img)

    if face is None:
        return "No Face"

    emb = resnet(face.unsqueeze(0)).detach()

    best_name = "Unknown"
    best_dist = 999

    for name, embeddings in known_embeddings.items():
        for known_emb in embeddings:
            dist = torch.dist(emb, known_emb).item()
            if dist < best_dist:
                best_dist = dist
                best_name = name

    if best_dist < 0.9:
        return best_name
    return "Unknown"