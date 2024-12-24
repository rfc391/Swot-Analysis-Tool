from transformers import pipeline

class SWOTAIHelper:
    def __init__(self):
        # Load a pre-trained model for text generation
        self.generator = pipeline("text-generation", model="gpt2")

    def suggest_swot(self, category, description, custom_prompt=None):
        """
        Suggest SWOT elements based on category, description, and an optional custom prompt.
        :param category: 'strength', 'weakness', 'opportunity', or 'threat'.
        :param description: Context or details for generation.
        :param custom_prompt: Optional custom prompt for AI.
        :return: A list of suggested SWOT elements.
        """
        if custom_prompt:
            prompt = f"{custom_prompt}: {description}"
        else:
            prompt = f"Generate {category} ideas based on this context: {description}"
        response = self.generator(prompt, max_length=100, num_return_sequences=1)
        suggestions = response[0]['generated_text'].split("\n")
        return suggestions

    def learn_from_user(self, user_data):
        """
        Simulate learning from user input for future enhancements (placeholder for AI training).
        :param user_data: User-provided SWOT elements.
        """
        # Future implementation: Train a lightweight model or fine-tune with user data.
        print(f"Learning from user data: {user_data}")