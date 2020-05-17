from flask import Flask, jsonify, request
import pandas as pd
import random


app = Flask(__name__)

data = pd.read_csv('head_100.csv')


@app.route('/')
def hello():
    return 'Добро пожаловать в эмулятор IMDB'


@app.route('/movie_id/<tconst>')
def search_by_id(tconst):
    response = data[data["tconst"] == tconst].to_dict('index')
    return jsonify(response)


@app.route('/movie/<title>')
def search_by_original_title(title):
    response = data[data["originalTitle"] == title]['tconst'].to_list()
    response = {'movie ' + title: response}
    return jsonify(response)


@app.route('/year/<year>')
def search_by_year(year):
    response = data[data["startYear"] == int(year)]['tconst'].to_list()
    response = {'year ' + year: response}
    return jsonify(response)


@app.route('/suggest/<count>', methods=['POST'])
def suggest_topk(count):
    count = int(count)
    l = list(range(100))
    content = request.get_json()
    for key in content.keys():
        l.remove(int(key[-3:]))
    response = {}
    for _ in range(count):
        number = random.choice(l)
        l.remove(number)
        response[number] = random.randint(0, 5)
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
