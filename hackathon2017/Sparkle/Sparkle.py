from flask import Flask, render_template, request
import requests
import json, urllib

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('homePage.html')

@app.route('/echo', methods=['POST'])
def hello_world():
    p = {'street-name': 'Commonwealth', 'city': 'Boston', 'state': 'MA', 'apikey': 'ESjW8PGyvKpXXpVc4VNx5j6alV9tJnT3'}
    response = requests.get(
    "https://apis.solarialabs.com/shine/v1/total-home-scores/reports", params=p)

    responseObj = json.loads(response._content)
    quiet_score = str(responseObj['totalHomeScores']['quiet']['value'])
    safety_score = str(responseObj['totalHomeScores']['safety']['value'])

    output = "The quiet score is " + quiet_score + ", and the safety score is " + safety_score+"."
    return render_template('homePage.html', address = request.form['address'])

@app.route('/action_page.php')
def calculate():
    return "hi"


if __name__ == '__main__':
    app.run()
