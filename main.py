import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    print(valutes)
    text = '<h1>Курс валют</h1>'
    text += '<table>'
    text += '<tr>'
    text += f'<th>Код 1</th>'
    text += f'<th>Код 2</th>'
    text += f'<th>Валюта</th>'
    text += f'<th>N%</th>'
    text += f'<th>Название</th>'
    text += f'<th>Покупка</th>'
    text += f'<th>Продажа</th>'
    text += f'<th>Разница покупки продажи</th>'
    text += '</tr>'
    for i in range(len(valutes)):
        text += '<tr>'
        difList = []
        for v in valutes[i].values():
            if type(v) == float:
                difList.append(v)
            text += f'<td>{v}</td>'
        text += f'<td>{str(round(difList[1]-difList[0],2))}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()
