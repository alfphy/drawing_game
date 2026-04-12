import time
import random

from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import numpy as np
from PyQt6 import QtGui

model = CLIPModel.from_pretrained("analyzer/clip")
processor = CLIPProcessor.from_pretrained("analyzer/clip")

def convert_qimage_to_pil(qimage):
    """Convert PyQt6 QImage to PIL Image"""
    from PIL import Image as PILImage
    qimage = qimage.convertToFormat(QtGui.QImage.Format.Format_ARGB32)
    width = qimage.width()
    height = qimage.height()
    ptr = qimage.bits()
    ptr.setsize(height * width * 4)
    arr = np.array(ptr).reshape(height, width, 4)
    arr = arr[:, :, [2, 1, 0, 3]]
    return PILImage.fromarray(arr, 'RGBA')


def get_category_prompts(category_name):
    """Get candidate prompts based on category"""
    from roundsetting import phrases
    
    if category_name == "Animals":
        prompts = [
            "a cat", "a dog", "a fish", "a bird", "a lion", "an elephant", "a monkey",
            "a giraffe", "a penguin", "a turtle", "a rabbit", "a bear", "a frog",
            "a pig", "a cow", "a mouse", "a duck", "a snake", "a spider", "a bee"
        ]
    elif category_name == "Flowers":
        prompts = [
            "a rose", "a tulip", "a daisy", "a sunflower", "a lotus", "a lily",
            "an orchid", "a cactus", "a mushroom", "a tree", "a leaf", "a palm tree",
            "a pine tree", "a branch", "a clover", "a vine", "a bamboo", "a fern",
            "ivy", "a bush"
        ]
    elif category_name == "Emoji":
        prompts = [
            "a happy smiley face", "a sad face", "an angry face", "a crying face",
            "a laughing face", "a face with heart eyes", "a face with sunglasses",
            "a surprised face", "a winking face", "a face blowing a kiss",
            "a sleeping face", "a sick face", "a nerdy face", "a cowboy face",
            "a clown face", "a skull", "a ghost", "an alien", "a robot", "a poop emoji"
        ]
    elif category_name == "Vehicles":
        prompts = [
            "a car", "a bus", "a train", "an airplane", "a helicopter",
            "a sailboat", "a ship", "a bicycle", "a motorcycle", "a dump truck",
            "a rocket", "a submarine", "a hot air balloon", "a scooter",
            "a skateboard", "a tractor", "an ambulance", "a fire truck",
            "a police car", "a taxi"
        ]
    else:
        prompts = ["a drawing"]
    
    return prompts


def analyze_drawing(image, category_name):
    """Analyze what CLIP sees in the drawing and return commentary"""
    prompts = get_category_prompts(category_name)
    
    start_time = time.time()
    inputs = processor(text=prompts, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    
    image_features = outputs.image_embeds
    text_features = outputs.text_embeds
    
    image_features = image_features / image_features.norm(dim=-1, keepdim=True)
    text_features = text_features / text_features.norm(dim=-1, keepdim=True)
    
    similarities = (image_features @ text_features.T)[0]
    similarities = similarities.cpu().detach().numpy()
    
    top_indices = similarities.argsort()[::-1][:3]
    top_scores = similarities[top_indices]
    top_prompts = [prompts[i] for i in top_indices]
    
    inference_time = (time.time() - start_time) * 1000
    print(f"CLIP analysis time: {inference_time:.0f}ms")
    print(f"Top matches: {list(zip(top_prompts, top_scores))}")
    
    return generate_commentary(top_prompts, top_scores)


def generate_commentary(top_prompts, top_scores):
    """Generate creative commentary based on CLIP's predictions"""
    
    uncertainty_words = [
        "hmm", "let me think...", "I'm not quite sure...", 
        "interesting...", "could it be...?", "maybe...",
        "I think I see...", "perhaps...", "is that...?"
    ]
    
    observation_words = [
        "I see", "It looks like", "That's giving me",
        "I can make out", "I notice", "It seems like"
    ]
    
    best_score = top_scores[0]
    second_score = top_scores[1]
    third_score = top_scores[2]
    
    target_phrase = top_prompts[0]
    
    if best_score > 0.28:
        return f"ooh nice! that's a {target_phrase}!"
    
    elif best_score > 0.24:
        uncertainty = random.choice(uncertainty_words)
        return f"{uncertainty} a {target_phrase}?"
    
    elif best_score > 0.20:
        observation = random.choice(observation_words)
        if second_score > 0.18:
            return f"{observation} a {target_phrase}... or maybe a {top_prompts[1]}?"
        return f"{observation} a {target_phrase}..."
    
    elif best_score > 0.16:
        uncertainty = random.choice(uncertainty_words)
        return f"{uncertainty} I'm not seeing it clearly yet..."
    
    else:
        return "waiting for you to draw..."


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

    # Get category prompts for top guess
    category_prompts = get_category_prompts(category) if category else ["a drawing"]
    
    # Combine all prompts
    all_prompts = [positive] + negatives + category_prompts
    start_time = time.time()
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
    neg_sim = similarities[1:4].mean().item()
    
    # Get top guess from category prompts (indices 4 onwards)
    category_sims = similarities[4:].cpu().detach().numpy()
    top_idx = category_sims.argmax()
    top_guess = category_prompts[top_idx]
    top_guess_score = category_sims[top_idx]

    # Calibrated score - direct similarity mapping
    # CLIP typically outputs 0.15-0.35 for drawings
    # Map: 0.15 → 0%, 0.40 → 100%
    score = max(0, min(100, (pos_sim - 0.15) * 400))

    end_time = time.time()
    inference_time =( end_time - start_time ) * 1000
    print(f"inference time: {inference_time}ms")
    print(f"Target: {positive}")
    print(f"Positive similarity: {pos_sim:.4f}")
    print(f"Negative avg: {neg_sim:.4f}")
    print(f"Score: {score:.2f}%")
    print(f"Top guess: {top_guess} ({top_guess_score:.4f})")

    return score, top_guess

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
