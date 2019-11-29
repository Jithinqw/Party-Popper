from flask import Flask, render_template
import csv
import random

app = Flask(__name__, static_folder='static')

@app.route("/")
def generate_employee():
    payload = {}
    with open('Sheet1.csv') as csv_file:
        rows = list(csv.reader(csv_file))
        random_employee = rows[random.randint(0, len(rows))]
        payload['id'],payload['name'] = random_employee[0], random_employee[3] + " " + random_employee[2]
    return render_template('index.html', message=payload)

if __name__ == "__main__":
    app.run(debug=True)
