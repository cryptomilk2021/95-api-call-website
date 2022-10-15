from flask import Flask, render_template
import datetime
import requests
from datetime import datetime

def where_is_ISS():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return render_template("index.html", image=where_is_ISS(), time=dt_string)

if __name__ == '__main__':
    app.run(debug=True)
