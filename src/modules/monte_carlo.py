
import numpy as np  
import pandas as pd  
import yfinance as yf  
from scipy.stats import norm  
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


plt.style.use('dark_background')


ticker = 'BTC-USD'  
start_date = "2020-01-01"  
end_date = "2024-01-01"  

def monte_carlo_pred(ticker,start_date,end_date,simul_length=300):
    data = yf.download(ticker, start=start_date, end=end_date)
    prices = data['Close']


    log_returns = np.log(1 + data['Close'].pct_change())
    u = log_returns.mean()  # Mean of returns
    var = log_returns.var()  # Variance of returns
    drift = u - (0.5 * var)  # Drift
    stdev = log_returns.std()  # Standard deviation of returns

    # =============================================================== Monte Carlo Simulation
    t_intervals = simul_length  # Simulation length (days)
    iterations = 10000

    # Aligning dimensions
    daily_returns = np.exp(
        drift + stdev * norm.ppf(np.random.rand(t_intervals, iterations))
    )


    last_price = prices.iloc[-1]  # Last known price
    price_paths = np.zeros_like(daily_returns)
    price_paths[0] = last_price

    for t in range(1, t_intervals):
        price_paths[t] = price_paths[t - 1] * daily_returns[t]


    final_prices = price_paths[-1]
    initial_price = last_price
    returns = (final_prices - initial_price) / initial_price * 100  # Returns in percentage

    # Normalizing frequency to probability
    bins = 30
    hist, bin_edges = np.histogram(returns, bins=bins, density=True)  # `density=True` normalizes data
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2  # Calculate bin centers


    hist_df = pd.DataFrame({
        'Final Return (%)': bin_centers,
        'Probability': hist
    })


    hist_fig = px.bar(
        hist_df,
        x='Final Return (%)',
        y='Probability',
        title="Final Returns Probability Distribution",
        labels={'Final Return (%)': 'Final Return (%)', 'Probability': 'Probability'},
        template="plotly_dark"  
    )


    hist_fig.add_vline(
        x=0, 
        line=dict(color="red", dash="dash"), 
        annotation_text="Initial Price (0%)",
        annotation_position="top left"
    )
    #hist_fig


    mcpred_fig = plt.figure(figsize=(10, 6))
    plt.plot(price_paths, alpha=0.7)  
    plt.title(f"Monte Carlo Simulation for {ticker}", color='white')
    plt.xlabel("Days", color='white')
    plt.ylabel("Simulated Price", color='white')
    plt.grid(alpha=0.3)
    #plt monte carlo

    # Value at Risk (VaR) for a 10% confidence level
    confidence_level = 0.1
    var_5 = np.percentile(returns, confidence_level * 100)

    es_5 = returns[returns <= var_5].mean()

    #outputs
    var_out = f"VaR 10%: {var_5:.2f}%"  # Maximum expected loss
    es5_out = f"Expected Shortfall 10%: {es_5:.2f}%"  # Average expected loss

    # Decision based on the probability of return above threshold
    threshold = 20  # %
    prob_positive = (returns > threshold).mean()
    print(f"Probability of return above {threshold}%:", prob_positive)
    if prob_positive > 0.6:  # 60% chance of return above the limit
        print("Decision: Invest based on Monte Carlo analysis.")
    else:
        print("Decision: Do not invest due to high risk or low return expectation.")

    # Answer the question at each point: "What is the probability that the final return will be less than or equal to X%?"
    hist_df['Cumulative Probability'] = hist_df['Probability'].cumsum() / hist_df['Probability'].sum()

    proba_fig = px.line(
        hist_df,
        x='Final Return (%)',
        y='Cumulative Probability',
        title="Cumulative Probability of Final Returns",
        labels={'Final Return (%)': 'Final Return (%)', 'Cumulative Probability': 'Cumulative Probability'},
        template="plotly_dark"  
    )
    # proba_fig.show()

    return hist_fig, mcpred_fig,proba_fig, var_out,es5_out
#====================================================================================================================================



ticker = 'BTC-USD'  
start_date = "2020-01-01"  
end_date = "2024-01-01"  

def monte_carlo_retro(ticker,start_date,end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    prices = data['Close']



    simulation_data = yf.download(ticker, start=start_date, end=end_date)
    real_prices = simulation_data['Close']


    log_returns = np.log(1 + data['Close'].pct_change())
    u = log_returns.mean()  
    var = log_returns.var()  
    drift = u - (0.5 * var)  
    stdev = log_returns.std()

    # Monte Carlo Simulation
    t_intervals = len(real_prices)  # Match simulation length to real data
    iterations = 100  

    daily_returns = np.exp(
        drift + stdev * norm.ppf(np.random.rand(t_intervals, iterations))
    )

    last_price = prices.iloc[-1]  # Last known price
    price_paths = np.zeros_like(daily_returns)
    price_paths[0] = last_price

    for t in range(1, t_intervals):
        price_paths[t] = price_paths[t - 1] * daily_returns[t]


    initial_real_price = real_prices.iloc[0]
    final_real_price = real_prices.iloc[-1]
    real_return = ((final_real_price - initial_real_price) / initial_real_price) * 100


    mc_fig = plt.figure(figsize=(12, 6))
    plt.plot(price_paths, alpha=0.3, color='blue', label='Simulated Paths')  # Simulated paths
    plt.plot(range(t_intervals), real_prices.values, color='yellow', linewidth=2, label='Real Performance')  # Real data
    plt.title(f"Monte Carlo Simulation vs Real Performance for {ticker}", color='white')
    plt.xlabel("Days", color='white')
    plt.ylabel("Price", color='white')


    plt.annotate(
        f"Real Return: {real_return:.2f}%",
        xy=(t_intervals - 1, final_real_price),
        xytext=(t_intervals - 1, final_real_price + 10),
        arrowprops=dict(facecolor='yellow', arrowstyle="->"),
        color='yellow',
        fontsize=10
    )


    plt.grid(alpha=0.3)
    # plt.show()


    final_prices = price_paths[-1]
    initial_price = last_price
    returns = (final_prices - initial_price) / initial_price * 100  

    confidence_level = 0.05
    var_5 = np.percentile(returns, confidence_level * 100)
    es_5 = returns[returns <= var_5].mean()

    var_out = f"VaR 10%: {var_5:.2f}%"  # Maximum expected loss
    es5_out = f"Expected Shortfall 10%: {es_5:.2f}%"  # Average expected loss

    # Decision based on probability of return above threshold
    threshold = 20  # %
    prob_positive = (returns > threshold).mean()
    print(f"Probability of return above {threshold}%:", prob_positive)
    if prob_positive > 0.6:  # 60% chance of return above the limit
        print("Decision: Invest based on Monte Carlo analysis.")
    else:
        print("Decision: Do not invest due to high risk or low return expectation.")

    return mc_fig,var_out,es5_out

description = '''

'''