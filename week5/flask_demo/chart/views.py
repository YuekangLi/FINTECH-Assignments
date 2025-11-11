import csv

from chart import app
from flask import render_template, jsonify, make_response, flash

@app.route('/')
def index():
    return render_template("index.html", page_data={"title": "Duke Blue Pay: Home"})

@app.route('/stock/')
@app.route('/stock/<symbol>')
def show_stock_info(symbol = None):
    if symbol:       
        page_data = {"title": "Duke Blue Pay: " + symbol, "inputValue": symbol}
        try:
            with open('chart/data/'+symbol.upper()+'.csv')  as csvfile:
                return render_template("stock.html", page_data=page_data, symbol=symbol) 
        except:
            # see https://flask.palletsprojects.com/en/3.0.x/patterns/flashing/#flashing-with-categories
            flash('Stock symbol not found: '+symbol,'error') 
    else:
        page_data = {"title": "Duke Blue Pay: Stock Information", "inputValue": ""}
    return render_template("stock.html", page_data=page_data)

@app.route('/stock/pricing/<symbol>')
def retrieve_stock_prices(symbol = None):
    close_prices = []
    dates = []

    try:
        with open('chart/data/'+symbol.upper()+'.csv')  as csvfile:
            stockreader = csv.DictReader(csvfile)
            for row in stockreader:
                dates.append(row["Date"])
                close_prices.append(row["Adj Close"])
            result = {
                "symbol": symbol,
                "dates": dates,
                "adjClosePrices": close_prices
            }
            return jsonify(result)
    except:
        return make_response(jsonify({'error': symbol+' - not found'}), 404)
