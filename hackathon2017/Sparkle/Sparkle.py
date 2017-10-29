from flask import Flask, render_template, request, redirect
import requests
import json
import urllib.request as ur
import random as random

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

    quiet_score = responseObj['totalHomeScores']['quiet']['value']
    safety_score = responseObj['totalHomeScores']['safety']['value']

    link = get_next_giphy(quiet_score, safety_score)

    return render_template('results.html', quiet_score=str(quiet_score), safety_score=str(safety_score), link=link)

@app.route('/index')
def index():
    return render_template('homePage.html')

@app.route('/action_page.php')
def calculate():
    return "hi"


def get_next_giphy(x, y):
    good_threshold = 40
    bad_threshold = 20

    API_KEY = "bv9xw5KEmBxkF8FglWO2dd9iAU0ze9Wr"
    limit = "1"
    offset = str(random.randrange(25))
    avg = (x + y) / 2

    if avg <= bad_threshold:
        search_term = "bad"

    elif avg > bad_threshold and avg < good_threshold:
        search_term = "not+bad"

    else:
        search_term = "awesome"

    data = json.loads(ur.urlopen(
        "http://api.giphy.com/v1/gifs/search?q=" + search_term + "&api_key=" + API_KEY + "&limit=" + limit + "&offset=" + offset).read())

    print(data['data'][0]['embed_url'])
    return data['data'][0]['embed_url']

if __name__ == '__main__':
    app.run()
