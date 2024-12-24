from transformers import pipeline

class SWOTAIHelper:
    def __init__(self):
        # Load a pre-trained model for text generation
        self.generator = pipeline("text-generation", model="gpt2")

    def suggest_swot(self, category, description):
        """
        Suggest SWOT elements based on the category and description provided.
        :param category: One of 'strength', 'weakness', 'opportunity', or 'threat'.
        :param description: Context or details to generate suggestions.
        :return: A list of suggested SWOT elements.
        """
        prompt = f"Generate {category} ideas for a business based on this context: {description}"
        response = self.generator(prompt, max_length=100, num_return_sequences=1)
        suggestions = response[0]['generated_text'].split("\n")
        return suggestions