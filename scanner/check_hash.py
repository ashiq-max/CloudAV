import hashlib
import sys
from pathlib import Path

MALWARE_DB = Path(__file__).parent / "malware_hashes.txt"

def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def load_malware_hashes():
    if not MALWARE_DB.exists():
        print("⚠️  malware_hashes.txt not found:", MALWARE_DB)
        return set()
    lines = MALWARE_DB.read_text(encoding="utf-8").splitlines()
    hashes = {line.strip().lower() for line in lines if line.strip()}
    print("✅ Loaded malware hashes:", hashes)
    return hashes

def check_file(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    h = sha256_of_file(path)
    malware_hashes = load_malware_hashes()
    is_infected = h.lower() in malware_hashes
    return {"path": str(path), "sha256": h, "infected": is_infected}

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_hash.py <file_path>")
        sys.exit(1)
    target = sys.argv[1]
    try:
        result = check_file(target)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
    print("\n--- Scan Result ---")
    print("File:", result["path"])
    print("SHA256:", result["sha256"])
    print("Status:", "INFECTED ⚠️" if result["infected"] else "CLEAN ✅")

if __name__ == "__main__":
    main()
