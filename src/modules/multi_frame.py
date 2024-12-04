import yfinance as yf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

macro_time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tickers = ["BBAS3", "CSNA3", "FLRY3", "ITSA4", "KEPL3", "KLBN4", "TAEE4", "UNIP3", "MXRF11", "VGIR11", "VALE3", 'GOAU4']
df = pd.DataFrame(index=macro_time)
## Charts
def analisar_serie_temporal_yahoo(ticker, janela_anos=5):
    """
    Analyzes a time series of stock prices obtained via Yahoo Finance,
    applying a rolling window and calculating the percentage difference.

    Parameters:
        ticker (str): Stock symbol (e.g., 'AAPL', 'MSFT').
        janela_anos (int): Number of years for the rolling window.

    Returns:
        media_diferenca_percentual (float): Average of the percentage differences between the first and last values of each window.
        dispersao_percentual (float): Standard deviation of the calculated percentage differences.
    """
    # Get historical data for the stock
    print(f"Downloading data for the asset: {ticker}...")
    df = yf.Ticker(ticker).history(period="max")
    
    if df.empty:
        raise ValueError("No data returned. Check if the ticker is correct.")

    # Ensure the index is reset (to handle date-based indices)
    df.reset_index(inplace=True)

    # Filter the necessary columns
    df = df[['Date', 'Close']]
    df.rename(columns={'Date': 'Data', 'Close': 'Preco'}, inplace=True)

    # Define the rolling window time in days (approximately 5 years)
    janela_dias = janela_anos * 252  # 252 trading days per year

    # List to store percentage differences
    diferencas_percentuais = []

    # Apply the rolling window
    for i in range(len(df) - janela_dias):
        janela = df.iloc[i:i + janela_dias]
        valor_inicial = janela['Preco'].iloc[0]
        valor_final = janela['Preco'].iloc[-1]
        diferenca_percentual = ((valor_final - valor_inicial) / valor_inicial) * 100
        diferencas_percentuais.append(diferenca_percentual)

    # Calculate the average and standard deviation of the percentage differences
    media_diferenca_percentual = np.median(diferencas_percentuais)
    dispersao_percentual = np.std(diferencas_percentuais)

    return media_diferenca_percentual#, dispersao_percentual



import plotly.graph_objects as go

def plotar_historico_acao(ticker):
    """
    Fetches and plots the historical closing prices of a stock using Yahoo Finance and Plotly.

    Parameters:
        ticker (str): Stock symbol (e.g., 'AAPL', 'MSFT').
    """
    # Fetch historical data for the stock
    print(f"Downloading data for the asset: {ticker}...")
    df = yf.Ticker(ticker).history(period="max")

    if df.empty:
        raise ValueError("No data returned. Check if the ticker is correct.")

    # Create a line chart with Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['Close'],
        mode='lines',
        name='Closing Price',
        line=dict(color='blue')
    ))

    # Chart settings
    fig.update_layout(
        title=f"Historical Closing Prices - {ticker}",
        xaxis_title="Date",
        yaxis_title="Closing Price (USD)",
        template="plotly_white",
        font=dict(size=14),
        hovermode="x"
    )

    # Display the chart
    fig.show()

# Example usage
ticker = "GOAU4.SA"  # Replace with the desired ticker
plotar_historico_acao(ticker)

# Jan 2019: 4.76
#==========================================================================
# USAGE TEST

# ticker = "BBAS3.SA"  # Example: Apple Inc.
# janela_anos = 5

# # # media, dispersao = analisar_serie_temporal_yahoo(ticker, janela_anos)
# media = analisar_serie_temporal_yahoo(ticker, janela_anos)


# for ticker in tickers:
#     ticker = ticker + '.SA'
#     df[ticker] = [analisar_serie_temporal_yahoo(ticker, time) for time in macro_time]

#=========================================================================

## Widgets

