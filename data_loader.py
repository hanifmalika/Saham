import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(f"{ticker}.JK")
    df = stock.history(
        period="1mo"
    )
    return df


if __name__ == "__main__":
    data = get_stock_data("BBCA")
    print(data.tail())