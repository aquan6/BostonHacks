from flask import Flask, render_template, request
import requests
import json, urllib

app = Flask(__name__)

@app.route('/')
def display():
    return render_template('homePage.html')

@app.route('/echo', methods=['POST'])
def user_input():
    streetnum = request.form['streetnum']
    streetname = request.form['streetname']
    city = request.form['city']
    state = request.form['state']

    p = {'street-number': streetnum, 'street-name': streetname, 'city': city, 'state': state, 'apikey': 'ESjW8PGyvKpXXpVc4VNx5j6alV9tJnT3'}
    response = requests.get("https://apis.solarialabs.com/shine/v1/total-home-scores/reports", params=p)
    responseObj = json.loads(response._content)

    quiet_score = str(responseObj['totalHomeScores']['quiet']['value'])
    safety_score = str(responseObj['totalHomeScores']['safety']['value'])

    return render_template('results.html', quiet_score=quiet_score, safety_score=safety_score)

@app.route('/action_page.php')
def calculate():
    return "hi"


if __name__ == '__main__':
    app.run()
