from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/time", methods=["GET"])
def find_time():
    current_time = datetime.datetime.now()
    time = current_time.strftime("%H:%M:%S")
    return jsonify(time)


@app.route("/date", methods=["GET"])
def find_date():
    current_date = datetime.datetime.now()
    date = current_date.strftime("%m-%d-%Y")
    return jsonify(date)


if __name__ == "__main__":
    app.run()
