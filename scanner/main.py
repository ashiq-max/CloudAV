# -*- coding: utf-8 -*-
import hashlib
import os
import requests

CLOUD_URL = "http://127.0.0.1:5000/check_hash"
LOCAL_DB = "malware_hashes.txt"

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def check_local_db(h):
    if not os.path.isfile(LOCAL_DB):
        return None
    try:
        with open(LOCAL_DB, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if parts[0] == h:
                    return {"status":"INFECTED", "malware_name": parts[1] if len(parts)>1 else "Unknown"}
    except Exception as e:
        print("Error reading local DB:", e)
    return None

def check_cloud(h):
    try:
        r = requests.post(CLOUD_URL, json={"hash": h}, timeout=5)
        if r.status_code == 200:
            return r.json()
        return {"status":"ERROR", "message": f"HTTP {r.status_code}"}
    except requests.RequestException as e:
        return {"status":"ERROR", "message": str(e)}

def scan(path):
    if not os.path.exists(path):
        print("File not found:", path)
        return
    h = calculate_sha256(path)
    print("SHA256:", h)

    local = check_local_db(h)
    if local:
        print("Result (local):", local)
        return

    cloud = check_cloud(h)
    if cloud.get("status") == "INFECTED":
      print("Result (cloud): INFECTED -", cloud.get("malware_name"))
    elif cloud.get("status") == "CLEAN":
        print("Result (cloud): CLEAN")
    else:
        print("Cloud check failed:", cloud)

if __name__ == "__main__":
    p = input("Enter the file path to scan: ").strip()
    scan(p)
