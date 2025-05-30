import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf


def get_valid_symbol(prompt):
    # Keep asking until the user enters a valid stock symbol (only letters)
    while True:
        symbol = input(prompt)
        if symbol.isalpha():
            return symbol.upper()
        print("Please enter a valid symbol using only alphabetic characters.")


def get_valid_input(prompt):
    # Keep asking until the user enters an integer value
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer value.")


def calculate_ema(df, short_ema=5, long_ema=13):
    # Calculate the short-term and long-term Exponential Moving Averages (EMA)
    df['ema_short'] = df['Close'].ewm(span=short_ema, adjust=False).mean()
    df['ema_long'] = df['Close'].ewm(span=long_ema, adjust=False).mean()

    # Create a column 'bullish' that is 1 when short EMA is above long EMA, else 0
    df['bullish'] = np.where(df['ema_short'] > df['ema_long'], 1.0, 0.0)

    # Calculate crossover signals: +1 when bullish trend starts, -1 when it ends
    df['crossover'] = df['bullish'].diff()


def show_graph(df, symbol, short_ema, long_ema):
    # Plot the closing price and EMAs, and mark buy/sell signals on the graph
    plt.figure(figsize=(12, 8))

    plt.plot(df.index, df['Close'], label='Close', color='blue')
    plt.plot(df.index, df['ema_short'], label=f'Short EMA ({short_ema})', color='orange')
    plt.plot(df.index, df['ema_long'], label=f'Long EMA ({long_ema})', color='purple')

    # Plot buy signals (crossover == 1) with green triangles
    plt.plot(df.index[df['crossover'] == 1.0], df['ema_short'][df['crossover'] == 1.0], '^', color='green', label='Buy')

    # Plot sell signals (crossover == -1) with red inverted triangles
    plt.plot(df.index[df['crossover'] == -1.0], df['ema_short'][df['crossover'] == -1.0], 'v', color='red',
             label='Sell')

    plt.title(f'{symbol} Price with Buy/Sell Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":

    # Get user inputs for stock symbol and EMA periods
    symbol = get_valid_symbol("Enter the stock symbol (e.g. AAPL): ")
    short_ema = get_valid_input("Enter the short-term EMA value: ")
    long_ema = get_valid_input("Enter the long-term EMA value: ")

    # Download historical stock data for the past 1 year using yfinance
    df = yf.download(symbol, period="1y")

    # Check if data was retrieved successfully
    if df.empty:
        print("Error: Invalid symbol or no data available.")
    else:
        # Calculate EMAs and trading signals
        calculate_ema(df, short_ema, long_ema)

        # Display the price chart with buy/sell signals
        show_graph(df, symbol, short_ema, long_ema)
