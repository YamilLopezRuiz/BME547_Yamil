from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/get_time/<patient_id>", methods=["GET"])
def find_time():
    return


@app.route("/get_date/<patient_id>", methods=["GET"])
def find_date():
    return


if __name__ == "__main__":
    app.run()
