from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get_results/<patient_id>", methods=["GET"])
def find_time():
    return