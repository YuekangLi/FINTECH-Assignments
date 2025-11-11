import requests

def get_closing_stock_prices(symbol, api_key):
    """
    Retrieve stock prices for a given symbol from Alpha Vantage.

    Args:
    - symbol (str): The stock symbol (e.g., AAPL for Apple Inc.).
    - api_key (str): Your Alpha Vantage API key.

    Returns:
    - dict: A dictionary containing stock prices.
    """
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if 'Time Series (Daily)' in data:
            closing_prices = {}
            for date, values in data['Time Series (Daily)'].items():
                if len(closing_prices) == 90:
                    break
                closing_prices[date] = values['4. close']
            return closing_prices
        else:
            print("Error: Could not fetch data. Check your symbol or API key.")
            return None
        
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

# Example usage
api_key = ''
symbol = 'AAPL'
stock_prices = get_closing_stock_prices(symbol, api_key)
if stock_prices:
    dates = sorted(stock_prices.keys(), reverse = True)
    for date in dates:
        print("{}: ${:.2f}".format(date,float(stock_prices[date])))

