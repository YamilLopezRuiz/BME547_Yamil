from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)


def find_datetime():
    current = datetime.now()
    return current


@app.route("/time", methods=["GET"])
def find_time():
    current_time = find_datetime()
    time = current_time.strftime("%H:%M:%S")
    return time


@app.route("/date", methods=["GET"])
def find_date():
    current_date = find_datetime()
    date = current_date.strftime("%m-%d-%Y")
    return date


@app.route("/age", methods=["POST"])
def add_handler():
    in_data = request.get_json()  # string
    input_date = in_data['date']
    input_date = datetime.strptime(input_date, "%m-%d-%Y")
    current_date = find_datetime()  # Current date
    date_diff = current_date - input_date
    difference = date_diff.days
    year_diff = difference / 365
    year_diff = round(year_diff, 2)
    return jsonify(year_diff)


@app.route("/until_next_meal/<meal>", methods=["GET"])
def find_until_next_meal(meal):
    current_time = find_datetime()  # Current datetime
    current_date = find_date()  # Current date string
    # Create meal date/time
    if meal == "breakfast":
        mealtime = current_date + " 8:0:0"
    elif meal == "lunch":
        mealtime = current_date + " 12:0:0"
    elif meal == "dinner":
        mealtime = current_date + " 20:0:0"
    print(mealtime)
    mealtime = datetime.strptime(mealtime, "%m-%d-%Y %H:%M:%S")
    time_diff = mealtime - current_time
    difference = time_diff.seconds
    meal_time = difference / 3600
    meal_time = round(meal_time, 2)
    return jsonify(meal_time)


if __name__ == "__main__":
    app.run()
