import csv
from flask import Flask, render_template, request

from data_scraper import get_api_data

app = Flask(__name__)

@app.route("/")
def main():
    data = get_api_data()
    context = {"currencies": [currency["code"] for currency in data]}
    return render_template("page.html", **context)

@app.route("/convert", methods=["GET"])
def convert():
    data = get_api_data()
    changes = dict((currency["code"], float(currency["bid"])) for currency in data)
    if request.method == "GET":
        currency = request.args["currency"]
        value = request.args["value"]
        if not value:
            value = 1.00
        cost = round(float(value) * changes[currency], 3)
        return render_template("result.html", currency=currency, value=value, cost=cost)

def get_data_from_csv(filename):
    data = []
    with open(filename) as f_obj:
        reader = csv.DictReader(f_obj, delimiter=";")
        for row in reader:
            data.append(row)
    return data

if __name__ == "__main__":
    app.run()