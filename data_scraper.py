import csv
import requests

URL = "http://api.nbp.pl/api/exchangerates/tables/C?format=json"

def get_api_data(url=URL):
    # Getting data
    response = requests.get(URL)
    data = response.json()
    # Extracting currencies data
    currencies = data[0]["rates"]
    return currencies

def save_to_file(data, filename="currencies.csv"):
    # Saving to csv file
    with open(filename, mode="w", encoding="utf-8", newline="") as f_obj:
        headers = [key for key in data[0]]
        writer = csv.DictWriter(f_obj, headers, delimiter=";")
        writer.writeheader()
        for currency in data:
            writer.writerow(currency)

if __name__ == "__main__":
    data = get_api_data()
    save_to_file(data)