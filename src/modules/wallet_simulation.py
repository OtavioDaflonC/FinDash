import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go

asset={}
def wallet_simulate(ativos, indices, data_comparacao):
    
    """
    Cria uma carteira com base nos ativos e compara sua performance com índices de mercado.

    Parâmetros:
        ativos (dict): Um dicionário onde as chaves são os tickers dos ativos 
                       e os valores são listas no formato [peso].
        indices (list): Lista de tickers de índices a serem comparados.
        data_comparacao (tuple): Datas de início e fim para a comparação, no formato ('AAAA-MM-DD', 'AAAA-MM-DD').

    Retorno:
        pd.DataFrame: DataFrame contendo o rendimento acumulado da carteira e dos índices.


        #=========================================================================
# for example:

# start = '2018-01-01'
# ativos = {
#     'BBAS3.SA': [ 0.209],  
#     'CSNA3.SA': [ 0.042],  
#     'FLRY3.SA': [  0.051],
#     'ITSA4.SA': [ 0.089],
#     'KEPL3.SA': [ 0.175],
#     'KLBN4.SA': [ 0.083],
#     'TAEE4.SA': [ 0.061],
#     'MGLU3.SA': [ 0.002],
#     'UNIP6.SA': [ 0.107],
#     'GOAU4.SA': [ 0.18],
 
# }

# indices = ['^GSPC', '^BVSP','^N225']  
# data_comparacao = (start, '2024-11-20') # datas de compra precisam ser antes da primeira data desse intervalo


#end example
#============================================================================
    """
    # Validar as datas
    data_inicio = pd.to_datetime(data_comparacao[0])  # Data de início definida pelo usuário
    data_fim = pd.to_datetime(data_comparacao[1])

    ptfnm = 'Portifolio' # portifolio name
    tickers = list(ativos.keys()) + indices
    dados = yf.download(tickers, start=data_inicio, end=data_fim)['Adj Close']

    # Preencher valores ausentes
    dados = dados.fillna(method='ffill').fillna(method='bfill')

    # Calcular retornos diários
    retornos_diarios = dados.pct_change().dropna()

    # Calcular pesos da carteira
    pesos_carteira = pd.Series({ticker: ativos[ticker][0] for ticker in ativos}).rename_axis("Ativos")
    pesos_carteira /= pesos_carteira.sum()

    # Calcular o retorno da carteira
    retorno_carteira = (retornos_diarios[list(ativos.keys())] @ pesos_carteira).rename(ptfnm)
    rendimento_acumulado = (1 + retorno_carteira).cumprod() - 1

    # Calcular o rendimento acumulado dos índices
    rendimento_indices = (1 + retornos_diarios[indices]).cumprod() - 1
    resultado = pd.concat([rendimento_acumulado, rendimento_indices], axis=1)
    resultado.index.name = "Data"


    fig = go.Figure()

    # Adicionar a performance da carteira
    fig.add_trace(go.Scatter(
        x=resultado.index,
        y=resultado[ptfnm],
        mode='lines',
        name='Carteira',
        line=dict(width=2, color='blue')
    ))


    for indice in indices:
        fig.add_trace(go.Scatter(
            x=resultado.index,
            y=resultado[indice],
            mode='lines',
            name=indice,
            line=dict(width=2)
        ))

    fig.update_layout(
        title="Performance Acumulada: Carteira vs Índices",
        xaxis_title="Data",
        yaxis_title="Rendimento Acumulado",
        template="plotly_white",
        legend_title="Legenda",
    )

    return fig

description = """
Welcome! Here is the place to simulate a portifolio's performance managing asset weights and time range freely.
You can add stocks, index funds, some cripto... whatever you like.

 You can search for the acceptable tickets at : https://finance.yahoo.com/
Please keep in mind that this dashboard will accept only yahoo finance asset terminology. e.g: A brazilian stock will need the
sufix '.SA' such as PETR4.SA.

Also you should write the date in  "DD/MM/YYYY" format.

Make sure you use a total of 100% assets for confirm scale at percentage.
"""