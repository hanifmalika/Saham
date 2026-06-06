from data_loader import get_stock_data

def red_streak(ticker, days):
    df = get_stock_data(ticker)
    closes = df['Close']
    
    for i in range(days):
        if closes.iloc[-(i+1)] >= closes.iloc[-(i+2)]:
            return False
    return True

if __name__ == "__main__":
    
    print(red_streak("BBCA", 3)
          )