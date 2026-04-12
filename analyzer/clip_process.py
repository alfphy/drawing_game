import time
import random

from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("analyzer/clip")
processor = CLIPProcessor.from_pretrained("analyzer/clip")


