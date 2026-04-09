from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

model = CLIPModel.from_pretrained("analyzer/clip")
processor = CLIPProcessor.from_pretrained("analyzer/clip")


def score_drawing(image, challenge_phrase, category=None):
    # Build positive prompt
    if category == "Emoji":
        positive = f"an emoji of {challenge_phrase}"
    elif category == "Animals":
        positive = f"a simple drawing of {challenge_phrase}"
    elif category == "Flowers":
        positive = f"a simple sketch of {challenge_phrase}"
    elif category == "Vehicles":
        positive = f"a simple drawing of {challenge_phrase}"
    else:
        positive = f"a drawing of {challenge_phrase}"

    # Negative prompts (what the drawing should NOT be)
    negatives = [
        "text or numbers on paper",
        "math equation or formula",
        "handwriting or words",
        "random scribbles",
    ]

    # Combine all prompts
    all_prompts = [positive] + negatives

    # Process image and text
    inputs = processor(text=all_prompts, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)

    # Get embeddings
    image_features = outputs.image_embeds
    text_features = outputs.text_embeds

    # Normalize
    image_features = image_features / image_features.norm(dim=-1, keepdim=True)
    text_features = text_features / text_features.norm(dim=-1, keepdim=True)

    # Calculate similarities
    similarities = (image_features @ text_features.T)[0]

    pos_sim = similarities[0].item()
    neg_sim = similarities[1:].mean().item()

    # Calibrated score
    calibrated = pos_sim - neg_sim

    # Map to 0-100 (calibrated range ~ -0.05 to 0.20)
    score = max(0, min(100, calibrated * 500))

    print(f"Target: {positive}")
    print(f"Positive similarity: {pos_sim:.4f}")
    print(f"Negative avg: {neg_sim:.4f}")
    print(f"Calibrated: {calibrated:.4f}")
    print(f"Score: {score:.2f}%")

    return score

# def score_drawing(image,challenge_phrase):
#
#
#     # Process image and text
#     inputs = processor(text=[challenge_phrase], images=image, return_tensors="pt", padding=True)
#
#     # Get embeddings (features)
#     outputs = model(**inputs, output_hidden_states=True)
#
#     # Extract image and text features
#     image_features = outputs.image_embeds
#     text_features = outputs.text_embeds
#
#     # Normalize
#     image_features = image_features / image_features.norm(dim=-1, keepdim=True)
#     text_features = text_features / text_features.norm(dim=-1, keepdim=True)
#
#     # Cosine similarity
#     similarity = (image_features @ text_features.T).item()
#
#     # CLIP similarity ranges ~0.1 to ~0.35
#     # Map to 0-100
#     score = max(0, min(100, (similarity - 0.1) * 400))
#
#     print(f"Similarity: {similarity:.4f}")
#     print(f"Score: {score:.2f}%")
