from flask import Flask, render_template, request, jsonify
from pdf_parser import extract_data
from db import collection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload-pdf', methods=['POST'])
def handle_data():
    if "file" not in request.files:
        return {"error": "No file provided"}, 400

    pdf_file = request.files["file"]
    data = extract_data(pdf_file.read())

    result = collection.insert_one(data)
    data["_id"] = str(result.inserted_id)

    return jsonify({
        "status": "success",
        "document_id": str(result.inserted_id),
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)