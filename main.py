import os
import json
import ollama

# ---------- Read draft ----------
with open("draft.txt", "r", encoding="utf-8") as f:
    draft = f.read()

# ---------- AI Improve ----------
prompt = f"""
You are a legal drafting assistant.
Improve the following legal draft professionally:

{draft}
"""

response = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': prompt}]
)

improved_text = response['message']['content']

# ---------- Local citation search ----------
data_folder = "data"
files = os.listdir(data_folder)

citation_text = "\n\n--- Relevant Case Law ---\n"

for file in files:
    with open(os.path.join(data_folder, file), "r", encoding="utf-8") as f:
        data = json.load(f)

        if "bail" in draft.lower() and "bail" in data["judgment_text"].lower():
            citation_text += data["case_title"] + "\n"

# ---------- Save final draft ----------
final_text = improved_text + citation_text

with open("final_ai_draft.txt", "w", encoding="utf-8") as f:
    f.write(final_text)

print("Final AI legal draft generated.")
