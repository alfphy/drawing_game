import time
import random

from PyQt6.QtCore import QThread, pyqtSignal

import analyzer.clip_process
from transformers import CLIPProcessor, CLIPModel
import numpy as np
import threading

#define the category and its possible phrase animals, flowers, vehicle, and emojis (not the target phrase)
#define the commentary


#Analyze the image (predict which specific phrases was that)
#Provide commentary (pass the analysis result)(if it was the target phrase tell "you almost there" do not include conclusive/confident statement if it is correct)(returns a string)

#thread that calls the commentary
CATEGORIES = {
    "animals": [
        "a cat", "a dog", "a bird", "a fish", "a rabbit",
        "a horse", "a butterfly", "an elephant", "a giraffe", "a lion",
        "a tiger", "a monkey", "a bear", "a penguin", "a turtle"
    ],
    "flowers": [
        "a rose", "a sunflower", "a tulip", "a daisy", "a lotus",
        "a lily", "a cherry blossom", "a dandelion", "a daffodil"
    ],
    "vehicles": [
        "a car", "a bus", "a bicycle", "a train", "an airplane",
        "a boat", "a helicopter", "a truck", "a motorcycle", "a rocket"
    ],
    "emojis": [
        "a smiley face", "a sad face", "a heart", "a star", "a thumbs up",
        "a peace sign", "a skull", "a ghost", "a crown", "a rainbow"
    ]
}

ALL_POSSIBLE_PHRASES = [phrase for phrases in CATEGORIES.values() for phrase in phrases]
UNCERTAINTY_WORDS = [
    "hmm", "let me think...", "I'm not quite sure...",
    "interesting...", "could it be...?", "maybe...",
    "I think I see...", "perhaps...", "is that...?"
]

OBSERVATION_WORDS = [
    "I see", "It looks like", "That's giving me",
    "I can make out", "I notice", "It seems like"
]

ALMOST_THERE_PHRASES = [
    "you're almost there!", "getting close!", "I can see it taking shape",
    "keep going!", "you're on the right track", "almost got it!"
]

from PIL import Image


def analyze_drawing(image, target_phrase):
    """Analyze the image and return commentary"""

    # Convert numpy array to PIL Image
    if isinstance(image, np.ndarray):
        if np.all(image == 255):
            return "waiting for you to draw..."
        pil_image = Image.fromarray(image.astype(np.uint8))
    else:
        pil_image = image

    # Include target phrase in the prompts
    target_with_a = f"a {target_phrase}" if not target_phrase.startswith(("a ", "an ")) else target_phrase
    all_phrases = ALL_POSSIBLE_PHRASES.copy()
    if target_with_a not in all_phrases:
        all_phrases.append(target_with_a)

    start_time = time.time()
    inputs = analyzer.clip_process.processor(text=all_phrases, images=pil_image, return_tensors="pt", padding=True)
    outputs = analyzer.clip_process.model(**inputs)

    image_features = outputs.image_embeds
    text_features = outputs.text_embeds

    image_features = image_features / image_features.norm(dim=-1, keepdim=True)
    text_features = text_features / text_features.norm(dim=-1, keepdim=True)

    similarities = (image_features @ text_features.T)[0]
    similarities = similarities.cpu().detach().numpy()

    top_indices = similarities.argsort()[::-1][:3]
    top_scores = similarities[top_indices].tolist()
    top_phrases = [all_phrases[i] for i in top_indices]

    inference_time = (time.time() - start_time) * 1000
    print(f"CLIP analysis time: {inference_time:.0f}ms")
    print(f"Top matches: {list(zip(top_phrases, top_scores))}")

    return generate_commentary(top_phrases, top_scores, target_with_a)

def generate_commentary(top_phrases, top_scores, target_phrase):
    """Generate creative commentary based on CLIP's predictions"""
    print("=== generate_commentary called ===")
    print(f"top_phrases: {top_phrases}")
    print(f"top_scores: {top_scores}")
    print(f"target_phrase: {target_phrase}")

    if not top_phrases or not top_scores:
        return "waiting for you to draw..."

    best_phrase = top_phrases[0]
    best_score = float(top_scores[0])  # Convert numpy float to Python float
    second_score = float(top_scores[1]) if len(top_scores) > 1 else 0
    second_phrase = top_phrases[1] if len(top_phrases) > 1 else None

    print(f"best_phrase: {best_phrase}")
    print(f"best_score: {best_score} ({type(best_score)})")

    # Check if the prediction matches the target phrase
    if best_phrase == target_phrase:
        return random.choice(ALMOST_THERE_PHRASES)

    # Not the target - provide uncertain observations
    if best_score > 0.28:
        uncertainty = random.choice(UNCERTAINTY_WORDS)
        return f"{uncertainty} {best_phrase}?"

    elif best_score > 0.24:
        observation = random.choice(OBSERVATION_WORDS)
        return f"{observation} {best_phrase}?"

    elif best_score > 0.20:
        observation = random.choice(OBSERVATION_WORDS)
        if second_score > 0.18:
            return f"{observation} {best_phrase}... or maybe {second_phrase}?"
        return f"{observation} {best_phrase}..."

    elif best_score > 0.16:
        uncertainty = random.choice(UNCERTAINTY_WORDS)
        return f"{uncertainty} I'm not seeing it clearly yet..."

    else:
        return "waiting for you to draw..."


class AnalysisWorker(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.image = None
        self.target_phrase = None
        self._is_running = True

    def set_data(self, image, target_phrase):
        self.image = image
        self.target_phrase = target_phrase
        self._is_running = True

    def run(self):
        try:
            commentary = analyze_drawing(self.image, self.target_phrase)
            if self._is_running:
                self.signal.emit(commentary)
        except Exception as e:
            print(f"Analysis error: {e}")
        finally:
            self._is_running = False

    def stop(self):
        self._is_running = False
        self.wait()













