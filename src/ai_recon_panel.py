from src.ai.swot_ai_engine import SWOTAI

def run_recon_panel():
    print("=== AI Recon Panel ===")
    ai = SWOTAI()

    while True:
        text = input("\nEnter SWOT note (or 'exit'): ")
        if text.lower() == 'exit':
            break
        label, confidence = ai.classify_entry(text)
        print(f"🧠 Classified as: {label} ({confidence * 100:.1f}% confidence)")

if __name__ == "__main__":
    run_recon_panel()