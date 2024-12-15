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
    """
    # Validar as datas
    data_inicio = pd.to_datetime(data_comparacao[0])  # Data de início definida pelo usuário
    data_fim = pd.to_datetime(data_comparacao[1])

    # Baixar os dados de mercado
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
    retorno_carteira = (retornos_diarios[list(ativos.keys())] @ pesos_carteira).rename("Carteira")
    rendimento_acumulado = (1 + retorno_carteira).cumprod() - 1

    # Calcular o rendimento acumulado dos índices
    rendimento_indices = (1 + retornos_diarios[indices]).cumprod() - 1

    # Combinar os resultados em um único DataFrame
    resultado = pd.concat([rendimento_acumulado, rendimento_indices], axis=1)
    resultado.index.name = "Data"

    # Criar o gráfico
    fig = go.Figure()

    # Adicionar a performance da carteira
    fig.add_trace(go.Scatter(
        x=resultado.index,
        y=resultado['Carteira'],
        mode='lines',
        name='Carteira',
        line=dict(width=2, color='blue')
    ))

    # Adicionar a performance dos índices
    for indice in indices:
        fig.add_trace(go.Scatter(
            x=resultado.index,
            y=resultado[indice],
            mode='lines',
            name=indice,
            line=dict(width=2)
        ))

    # Configurar o layout do gráfico
    fig.update_layout(
        title="Performance Acumulada: Carteira vs Índices",
        xaxis_title="Data",
        yaxis_title="Rendimento Acumulado",
        template="plotly_white",
        legend_title="Legenda",
    )

    return fig



