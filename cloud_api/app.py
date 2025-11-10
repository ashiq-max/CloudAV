from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample malware hash database
malware_db = {
    "4e461d548d3013ba9334589e2805afa9327a5ec8046a8e561c492758726b3aa4": "Trojan.Generic",
    "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92": "Ransomware.Test",
    "572a95fee9c0f320030789e4883707affe12482fbb1ea04b3ea8267c87a890fb": "Fake.TestMalware"
}
@app.route('/check_hash', methods=['POST'])
def check_hash():
    data = request.get_json()
    file_hash = data.get("hash")
    
    if file_hash in malware_db:
        return jsonify({"status": "INFECTED", "malware_name": malware_db[file_hash]})
    else:
        return jsonify({"status": "CLEAN"})

if __name__ == '__main__':
    app.run(debug=True)
