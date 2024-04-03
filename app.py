from flask import Flask, jsonify, render_template
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options\

import requests

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


def find_price():
    r = requests.get("https://www.alphaquery.com/stock/AAPL/price-chart-technicals")
    soup = BeautifulSoup(r.content,'html.parser')

    s = soup.find(id="quote-price-container")
    return(s.text)

@app.route('/get-stock-price')
def stock_price_route():
    price = find_price()
    return jsonify({'price':price})

if __name__ == '__main__':
    app.run(debug=True)