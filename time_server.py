from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
def find_datetime():
    current = datetime.datetime.now()
    return current

@app.route("/time", methods=["GET"])
def find_time():
    current_time = find_datetime()
    time = current_time.strftime("%H:%M:%S")
    return time


@app.route("/date", methods=["GET"])
def find_date():
    current_date = find_datetime()
    date = current_date.strftime("%m/%d/%Y")
    return date


@app.route("/age", methods=["POST"])
def add_handler():
    in_data = request.get_json()  # string
    input_date = in_data['date']
    input_date = datetime.datetime.strptime(input_date, "%m/%d/%Y")
    current_date = find_datetime()  # Current date
    date_diff = current_date - input_date
    difference = date_diff.days
    year_diff = difference / 365
    year_diff = round(year_diff, 2)
    return jsonify(year_diff)


if __name__ == "__main__":
    app.run()
