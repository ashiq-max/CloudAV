import hashlib
import requests
import os

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def scan_file(file_path):
    # Step 1: Calculate hash
    file_hash = calculate_sha256(file_path)
    print(f"\nFile: {file_path}")
    print(f"SHA256: {file_hash}")

    # Step 2: Send hash to cloud API
    url = "http://127.0.0.1:5000/check_hash"
    try:
        response = requests.post(url, json={"hash": file_hash})
        if response.status_code == 200:
            data = response.json()
            status = data.get("status", "UNKNOWN")
            if status == "INFECTED":
                print(f"⚠️  Status: INFECTED ({data.get('malware_name')})")
            else:
                print("✅ Status: CLEAN")
        else:
            print("Error: Server returned status", response.status_code)
    except Exception as e:
        print("❌ Could not connect to cloud API:", e)

if __name__ == "__main__":
    path = input("Enter the file path to scan: ").strip()
    if os.path.exists(path):
        scan_file(path)
    else:
        print("File not found. Please enter a valid path.")
