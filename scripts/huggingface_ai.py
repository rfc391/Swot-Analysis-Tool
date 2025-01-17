
from transformers import pipeline

# Initialize a code generation pipeline using a Hugging Face model
def generate_code(prompt):
    """
    Generates code based on the provided prompt using Hugging Face Transformers.
    """
    try:
        generator = pipeline("text-generation", model="Salesforce/codegen-350M-mono")
        response = generator(prompt, max_length=150, num_return_sequences=1)
        return response[0]["generated_text"]
    except Exception as e:
        print(f"Error generating code: {e}")
        return ""

def main():
    """
    Demonstrates AI-assisted code generation.
    """
    prompt = "Write a Python function to compute the factorial of a number."
    print(f"Prompt: {prompt}\n")
    generated_code = generate_code(prompt)
    print(f"Generated Code:\n{generated_code}")

if __name__ == "__main__":
    main()
