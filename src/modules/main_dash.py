import dash
import pandas as pd
from dash import html, dcc, Input, Output
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from modules.multi_frame import *
from utils import *

#=========================================================================
#multi_frame



dash.register_page(
    __name__,
    path="/main",  # main path
    name="Dashboard",
)

# Gerar arrays predefinidos
grath_xsize = 1000
def generate_random_data(size=1000):
    x = list(range(size))
    y = (np.cumsum(np.random.normal(0, 2, size))**2 +1) /90 # Série estocástica acumulada
    return x, y
# Dados predefinidos
predefined_x, predefined_y = generate_random_data()

# Criar layout do gráfico inicial com um ponto
def create_fig_with_point(index):
    fig = go.Figure(
        layout=go.Layout(
            xaxis=dict(
                visible=False,
                range=[0, grath_xsize],  # Scale
            ),
            yaxis=dict(
                visible=False,
                range=[0, 50],  # Scale
            ),
            margin=dict(t=0, b=0, l=0, r=0),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=predefined_x[:index],
            y=predefined_y[:index],
            mode="lines",
            line=dict(color="lime", width=2),
        )
    )
    return fig

# Gerando os dados
predefined_x, predefined_y = generate_random_data()

# Criando o gráfico estático com os dados predefinidos

# Criando o gráfico com os dados predefinidos
# fig_animation = create_static_animation(predefined_x, predefined_y)

# Gráfico de exemplo
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=["01/01/2024", "01/03/2024", "01/05/2024", "01/07/2024", "01/11/2024"],
        y=[0.5, 0.7, 1.2, 2.5, 3.5],
    )
)

# Main layout
layout = html.Div(
    style={"backgroundColor": "#1e1e1e", "color": "#FFFFFF", "fontFamily": "Arial"},
    children=[
        # Header
        html.Div(
            style={
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "space-between",
                "padding": "10px 20px",
                "backgroundColor": "#2c2c2c",
                "borderRadius": "10px",
                "marginBottom": "20px",
                "position": "relative",
            },
            children=[
                html.Img(
                    src="./assets/findash_img.png",
                    alt="FinDash Logo",
                    style={"height": "50px","zIndex": "1"},
                ),
                html.H1(
                    "FinDash",
                    style={"margin": "0", "fontSize": "24px", "color": "#FFFFFF","zIndex": "1"},
                ),
                dcc.Graph(
                    id="header-animation",
                    figure=create_fig_with_point(1),  # Inicializa com o primeiro ponto
                    style={
                        "position": "absolute",  # Mantém o posicionamento relativo à div pai
                        "top": "10%",  # Deixa 10% de espaço a partir do topo da div pai
                        "left": "10%",  # Deixa 10% de espaço a partir da margem esquerda da div pai
                        "height": "80%",  # Limita a altura do gráfico para 80% da altura da div pai
                        "width": "80%",  # Limita a largura do gráfico para 80% da largura da div pai
                        "pointerEvents": "none",  # Torna o gráfico não interativo
                        "zIndex": "0",  # Garante que o gráfico fique atrás de outros elementos
                    },
                    config={"staticPlot": True},  # Remove interatividade
                ),

                dcc.Interval(
                    id="interval-update",
                    interval=300,  # update animation time
                    n_intervals=0,  # Inicialização
                ),
            ],
        ),
        # Main content
        html.Div(
            style={"display": "flex", "padding": "20px", "gap": "20px"},
            children=[
                # Sidebar
                html.Div(
                    style={"width": "20%", "backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "10px"},
                    children=[
                        html.H4("Select your stocks", style={"textAlign": "center"}),
                        dcc.Input(
                            id="input-stocks",
                            type="text",
                            placeholder="Digite os tickers separados por vírgulas (ex: AAPL, TSLA, MSFT)",
                            style={"width": "100%"}
                        ),
                        html.Label("Analysis Options"),
                        # Botões para selecionar os gráficos
                        html.Div(
                            style={"display": "flex", "flexDirection": "column", "gap": "10px", "marginTop": "20px"},
                            children=[
                                html.Button("Multi Frame", id="multi_frame", n_clicks=0, style={"padding": "10px"}),
                                html.Button("option2", id="opt2", n_clicks=0, style={"padding": "10px"}),
                            ],
                        ),

                    ],
                ),
                # Main Content
                html.Div(
                    style={"width": "75%", "padding": "10px", "borderRadius": "10px"},
                    children=[
                        html.Div(
                            style={"display": "grid", "gridTemplateColumns": "repeat(4, 1fr)", "gap": "10px"},
                            children=[
                                html.Div(
                                    style={"backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "5px"},
                                    children=[
                                        html.H6("variable4", style={"textAlign": "center"}),
                                        html.H3("value", style={"textAlign": "center"}),
                                    ],
                                ),
                                html.Div(
                                    style={"backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "5px"},
                                    children=[
                                        html.H6("variable3", style={"textAlign": "center"}),
                                        html.H3("value", style={"textAlign": "center"}),
                                    ],
                                ),
                                html.Div(
                                    style={"backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "5px"},
                                    children=[
                                        html.H6("variable", style={"textAlign": "center"}),
                                        html.H3("value", style={"textAlign": "center"}),
                                    ],
                                ),
                                html.Div(
                                    style={"backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "5px"},
                                    children=[
                                        html.H6("variable2", style={"textAlign": "center"}),
                                        html.H3("value", style={"textAlign": "center"}),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            style={"marginTop": "20px"},
                            children=[
                                    html.H1("Dashboard com Loading Page", style={"textAlign": "center"}),
                                    dcc.Loading(
                                        id="loading-indicator",
                                        type="circle",  # Tipo de indicador: "circle", "dot" ou "default"
                                        children=[
                                            dcc.Graph(id="main-graph", figure=create_placeholder_figure()),
                                        ],
                                        style={"marginTop": "20px"},
                                    ),  # Adicionando ID ao gráfico
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)


@dash.callback(
    Output("header-animation", "figure"),
    Input("interval-update", "n_intervals"),
)
def update_header_animation(n_intervals):
    # Limitar o índice ao tamanho dos dados
    index = min(n_intervals + 1, len(predefined_x))
    return create_fig_with_point(index)

@dash.callback(
    Output("main-graph", "figure"),  # Atualiza o gráfico principal
    [
        Input("multi_frame", "n_clicks"),  # Botão Multi Frame
        Input("opt2", "n_clicks"),        # Outro botão
        Input("input-stocks", "value"),  # Entrada do campo de texto
    ],
)
def update_graph(btn1_clicks, btn2_clicks, ticker_input):
    ctx = dash.callback_context
    if not ctx.triggered:
        return fig  # Retorna o gráfico padrão se nenhuma interação ocorreu

    # Determinar qual entrada disparou o callback
    triggered_input = ctx.triggered[0]["prop_id"].split(".")[0]

    if triggered_input == "multi_frame":
        return create_placeholder_figure()  # Gráfico específico para o botão Multi Frame
    elif triggered_input == "opt2":
        return create_fig_with_point(50)  # Exemplo de alternativa
    elif triggered_input == "input-stocks" and ticker_input:
        # Lógica para atualizar o gráfico com base no campo de texto
        for ticker in ticker_input.split(","):  # Suporta múltiplos tickers separados por vírgulas
            ticker = ticker.strip() + ".SA"
            df[ticker] = [analisar_serie_temporal_yahoo(ticker, time) for time in macro_time]

        return px.line(df)  # Gráfico atualizado com os dados fornecidos

    return fig  # Retorna o gráfico padrão como fallback

# @dash.callback(
#     Output("main-graph", "figure"),  # Atualiza o gráfico principal
#     [Input("multi_frame", "n_clicks"), Input("opt2", "n_clicks")],  # Botões como entrada
#     allow_duplicate=True
# )
# def update_graph(btn1_clicks, btn2_clicks):
#     # Determinar qual botão foi clicado
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         return fig  # Retorna o gráfico padrão se nenhum botão foi clicado
#     else:
#         button_id = ctx.triggered[0]["prop_id"].split(".")[0]

#     # Atualizar o gráfico com base no botão clicado
#     if button_id == "multi_frame":
#         return fig  # Substitui pelo gráfico definido
#     elif button_id == "opt2":
#         # Substituir por outro gráfico, se necessário
#         return create_fig_with_point(50)  # Exemplo de gráfico com 50 pontos

#     return fig  # Retorna o gráfico padrão se nenhuma condição foi atendida

# # Callbacks
# @dash.callback(
#     Output("main-graph", "figure"),  # Atualiza o gráfico principal
#     Input("input-stocks", "value"),  # Entrada do campo de texto
#     allow_duplicate=True
# )
# def update_graph(ticker):

#     for ticker in tickers:
#         ticker = ticker + '.SA'
#         df[ticker] = [analisar_serie_temporal_yahoo(ticker, time) for time in macro_time]

#         multi_frame_fig = px.line(df)
#         return multi_frame_fig