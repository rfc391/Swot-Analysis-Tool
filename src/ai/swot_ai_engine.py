import re
import torch
from transformers import pipeline

class SWOTAI:
    def __init__(self, offline=False):
        self.offline = offline
        if not offline:
            try:
                self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
            except Exception as e:
                print("Warning: Falling back to basic SWOT classifier.", e)
                self.classifier = None

    def classify_entry(self, text):
        labels = ["Strength", "Weakness", "Opportunity", "Threat"]
        if self.classifier:
            result = self.classifier(text, candidate_labels=labels)
            return result['labels'][0], result['scores'][0]
        else:
            # Simple fallback logic
            text = text.lower()
            if any(word in text for word in ["advantage", "strong", "capable"]):
                return "Strength", 0.6
            elif any(word in text for word in ["limitation", "lack", "poor"]):
                return "Weakness", 0.6
            elif any(word in text for word in ["opportunity", "growth", "emerging"]):
                return "Opportunity", 0.6
            elif any(word in text for word in ["threat", "risk", "danger"]):
                return "Threat", 0.6
            else:
                return "Uncertain", 0.3

    def batch_classify(self, texts):
        return [self.classify_entry(text) for text in texts]