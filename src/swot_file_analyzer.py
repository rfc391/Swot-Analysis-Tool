import os
import time
from src.ai.swot_ai_engine import SWOTAI

WATCH_DIRS = ["/dropzone", "/classified"]
OUTPUT_DIR = "/classified/ai_analysis"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def analyze_file(filepath, ai):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        results = []
        for line in lines:
            label, confidence = ai.classify_entry(line.strip())
            results.append(f"{label} ({confidence*100:.1f}%): {line.strip()}")

        out_path = os.path.join(OUTPUT_DIR, os.path.basename(filepath) + ".ai.txt")
        with open(out_path, "w", encoding="utf-8") as out:
            out.write("\n".join(results))

        print(f"✅ Processed: {filepath} → {out_path}")
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")

def run_file_analyzer():
    ai = SWOTAI(offline=True)
    seen_files = set()

    print("📂 Watching /dropzone and /classified for new SWOT text files...")

    while True:
        for watch_dir in WATCH_DIRS:
            if not os.path.exists(watch_dir):
                continue

            for file in os.listdir(watch_dir):
                path = os.path.join(watch_dir, file)
                if path.endswith(".txt") and path not in seen_files:
                    analyze_file(path, ai)
                    seen_files.add(path)

        time.sleep(10)

if __name__ == "__main__":
    run_file_analyzer()