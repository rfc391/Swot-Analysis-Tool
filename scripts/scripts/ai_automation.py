
import openai
import os
import subprocess

# Initialize OpenAI API (Replace YOUR_API_KEY with a valid key)
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY")

def generate_code(prompt):
    """
    Uses OpenAI API to generate code based on a given prompt.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating code: {e}")
        return ""

def auto_update_dependencies():
    """
    Automatically updates dependencies using pip and logs changes.
    """
    try:
        subprocess.run(["pip", "list", "--outdated"], check=True)
        subprocess.run(["pip", "install", "--upgrade", "-r", "requirements.txt"], check=True)
        print("Dependencies updated successfully.")
    except Exception as e:
        print(f"Error updating dependencies: {e}")

def auto_test_and_fix():
    """
    Runs tests and generates fixes for detected issues.
    """
    try:
        result = subprocess.run(["pytest"], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            prompt = f"Fix the following test errors: {result.stderr}"
            fix_code = generate_code(prompt)
            print(f"Suggested Fix:
{fix_code}")
    except Exception as e:
        print(f"Error running tests: {e}")

# Main Automation Workflow
if __name__ == "__main__":
    print("Starting AI-driven automation...")
    auto_update_dependencies()
    auto_test_and_fix()
