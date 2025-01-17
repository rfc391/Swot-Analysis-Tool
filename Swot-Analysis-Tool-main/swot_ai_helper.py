
from transformers import pipeline

class SWOTAIHelper:
    def __init__(self):
        self.classifier = pipeline("text-classification", model="distilbert-base-uncased")

    def suggest_swot(self, category, description):
        categories = {
            "strength": ["advantage", "unique", "expertise", "resource"],
            "weakness": ["limitation", "disadvantage", "lacking", "improvement"],
            "opportunity": ["potential", "growth", "expansion", "trend"],
            "threat": ["risk", "competition", "challenge", "obstacle"]
        }
        
        prompt = f"Analyze this business aspect: {description}"
        result = self.classifier(prompt)[0]
        
        suggestions = []
        if result['score'] > 0.7:
            suggestions.append(f"Based on AI analysis: This appears to be a valid {category}")
            
        return suggestions
