import json, glob, sys
from difflib import SequenceMatcher

# Auto-detect file
files = glob.glob("*_investigation.json")
if not files:
    print("❌ No investigation JSON file found.")
    sys.exit()

filename = files[0]
print(f"📂 Loading results from {filename}")

# Load
with open(filename, "r", encoding="utf-8") as f:
    raw = json.load(f)

if isinstance(raw, str):
    data = json.loads(raw)
else:
    data = raw

query = input("\nAsk a question about the investigation: ").lower()

found = False
for item in data:
    if not isinstance(item, dict) or "claim" not in item:
        continue

    claim_text = item["claim"].lower()
    similarity = SequenceMatcher(None, query, claim_text).ratio()

    if similarity > 0.3 or any(word in claim_text for word in query.split()):
        found = True
        print(f"\n🟢 Claim: {item['claim']}")
        print(f"   Confidence: {item.get('confidence', 'N/A')}")
        for src in item.get("sources", []):
            print(f"   - Source: {src.get('url')}")
if not found:
    print("\n⚠️ No relevant claims found.")
