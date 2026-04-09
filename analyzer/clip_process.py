from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

model = CLIPModel.from_pretrained("analyzer/clip")
processor = CLIPProcessor.from_pretrained("analyzer/clip")
def score_drawing(image,challenge_phrase):
    # Process image and text
    inputs = processor(text=[challenge_phrase], images=image, return_tensors="pt", padding=True)

    # Get embeddings (features)
    outputs = model(**inputs, output_hidden_states=True)

    # Extract image and text features
    image_features = outputs.image_embeds
    text_features = outputs.text_embeds

    # Normalize
    image_features = image_features / image_features.norm(dim=-1, keepdim=True)
    text_features = text_features / text_features.norm(dim=-1, keepdim=True)

    # Cosine similarity
    similarity = (image_features @ text_features.T).item()

    # CLIP similarity ranges ~0.1 to ~0.35
    # Map to 0-100
    score = max(0, min(100, (similarity - 0.1) * 400))

    print(f"Similarity: {similarity:.4f}")
    print(f"Score: {score:.2f}%")
