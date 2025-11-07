# ☁️ CloudAV – Hybrid Antivirus System

**Author:** Mohan Sai  
**Course:** BCA – 5th Semester  
**Subject:** DCA3104 – Python Programming  
**Session:** April 2025  
**GitHub Repo:** [ashiq-max/CloudAV](https://github.com/ashiq-max/CloudAV)

---

## 🧠 Overview

**CloudAV** is a hybrid antivirus system that combines **local file hash scanning** and **cloud verification**.  
This project demonstrates the basic working of modern antivirus logic — using SHA-256 hashing, malware signature databases, and an optional cloud backend.

---

## ⚙️ Features

✅ **File Hash Scanning (Local):**  
Checks the SHA-256 hash of any file and compares it to a known malware list.

✅ **Graphical Interface (GUI):**  
Built with Tkinter — lets users easily select and scan files.

✅ **Customizable Malware Database:**  
Modify `malware_hashes.txt` to test your own file hashes.

✅ **Cloud Ready (Phase 3):**  
Prepared for a Flask-based cloud API to extend scanning remotely.

---

## 🧩 Project Structure





---

## 🧰 Technologies Used
- Python 3.12+
- Tkinter (for GUI)
- Hashlib (for SHA-256)
- Requests (for future cloud API)
- PowerShell / Visual Studio

---

## 🚀 How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ashiq-max/CloudAV.git
cd CloudAV
