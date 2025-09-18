import os, json

INPUT_DIR = "./"
OUTPUT_FILE = "manifest.json"

manifest = {}

for fname in os.listdir(INPUT_DIR):
    if not fname.lower().endswith(".webp"):
        continue

    # filename looks like "a-guakhmaz-azerbaijan.webp"
    letter = fname[0].lower()
    manifest.setdefault(letter, []).append(fname)

# sort each list for consistency
for letter in manifest:
    manifest[letter].sort()

with open(OUTPUT_FILE, "w") as f:
    json.dump(manifest, f, indent=2)

print(f"✅ Manifest written to {OUTPUT_FILE}")
