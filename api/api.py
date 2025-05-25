from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Load JSON data at startup
MARKS_FILE = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')

with open(MARKS_FILE, 'r') as f:
    marks_data = json.load(f)

@app.route("/", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    result = [marks_data.get(name, None) for name in names]
    return jsonify({"marks": result})
