# Stock Analysis Tool

This Python project fetches historical stock data using the **yfinance** library and performs technical analysis using Exponential Moving Averages (EMA). 
The tool helps identify buy and sell signals based on the crossover of short-term and long-term EMAs. It also visualizes the stock price along with these signals using **Matplotlib**.

## Features
- Download historical stock data automatically with yfinance.
- Calculate short-term and long-term EMAs.
- Detect buy and sell signals from EMA crossovers.
- Plot price data and signals for easy interpretation.

## Requirements
- Python 3.x
- yfinance
- pandas
- numpy
- matplotlib

## How to use
Run the script and input the stock symbol and EMA parameters when prompted. The program will fetch the data, analyze it and display a graph.
