import dash
import pandas as pd
from dash import html, dcc, Input, Output, State
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from modules.multi_frame import *
from utils import *


dash.register_page(
    __name__,
    path="/multi-frame",  # main path
    name="multi-frame_Dashboard",
)


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
                    style={"height": "50px", "zIndex": "1"},
                ),
                html.H1(
                    "FinDash",
                    style={
                        "margin": "0",
                        "fontSize": "28px",
                        "fontWeight": "bold",
                        "color": "#FFFFFF",
                        "zIndex": "1",
                    },
                ),
                dcc.Graph(
                    id="header-animation",
                    figure=create_fig_with_point(1),
                    style={
                        "position": "absolute",
                        "top": "10%",
                        "left": "10%",
                        "height": "80%",
                        "width": "80%",
                        "pointerEvents": "none",
                        "zIndex": "0",
                    },
                    config={"staticPlot": True},
                ),
                dcc.Interval(
                    id="interval-update",
                    interval=300,
                    n_intervals=0,
                ),
            ],
        ),
        # Main content
        html.Div(
            style={"display": "flex", "padding": "20px", "gap": "20px"},
            children=[
                # Sidebar
                html.Div(
                    style={
                        "width": "20%",
                        "backgroundColor": "#2c2c2c",
                        "padding": "15px",
                        "borderRadius": "10px",
                    },
                    children=[
                        html.H4(
                            "Select assets",
                            style={"textAlign": "center", "marginBottom": "20px", "fontSize": "18px"},
                        ),
                        dcc.Input(
                            id="input-stocks",
                            type="text",
                            placeholder="Digite os tickers separados por vírgulas (ex: AAPL, TSLA, MSFT)",
                            style={
                                "width": "100%",
                                "padding": "10px",
                                "marginBottom": "10px",
                                "borderRadius": "5px",
                                "border": "1px solid #ccc",
                            },
                        ),
                        html.Button(
                            "Calcular",
                            id="calculate-button2",
                            n_clicks=0,
                            style={
                                "width": "100%",
                                "padding": "10px",
                                "backgroundColor": "#007BFF",
                                "color": "white",
                                "border": "none",
                                "borderRadius": "5px",
                                "cursor": "pointer",
                                "fontSize": "16px",
                                "marginBottom": "20px",
                            },
                        ),
                        html.H5(
                            "Opções de análise",
                            style={"marginBottom": "10px", "color": "#FFFFFF", "fontSize": "16px"},
                        ),
                        html.Div(
                            style={"display": "flex", "flexDirection": "column", "gap": "10px"},
                            children=[
                                dcc.Link(
                                    html.Button(
                                        "Wallet Simulation",
                                        id="wallet_simulation",
                                        n_clicks=0,
                                        style={
                                            "padding": "10px",
                                            "borderRadius": "5px",
                                            "backgroundColor": "#3a3a3a",
                                            "color": "white",
                                            "fontSize": "14px",
                                        },
                                    ),
                                    href='/wallet-simulation'
                                ),
                                dcc.Link(
                                    html.Button(
                                        "Multi-Frame",
                                        id="multi_frame",
                                        n_clicks=0,
                                        style={
                                            "padding": "10px",
                                            "borderRadius": "5px",
                                            "backgroundColor": "#3a3a3a",
                                            "color": "white",
                                            "fontSize": "14px",
                                        },
                                    ),
                                    href='/multi-frame'
                                ),
                                dcc.Link(
                                    html.Button(
                                        "Monte Carlo Pred",
                                        id="monte_carlo",
                                        n_clicks=0,
                                        style={
                                            "padding": "10px",
                                            "borderRadius": "5px",
                                            "backgroundColor": "#3a3a3a",
                                            "color": "white",
                                            "fontSize": "14px",
                                        },
                                    ),
                                    href='/mtcarlo'
                                ),
                                dcc.Link(
                                    html.Button(
                                        "Midia Pred",
                                        id="midia_pred",
                                        n_clicks=0,
                                        style={
                                            "padding": "10px",
                                            "borderRadius": "5px",
                                            "backgroundColor": "#3a3a3a",
                                            "color": "white",
                                            "fontSize": "14px",
                                        },
                                    ),
                                    href='/midia_pred'
                                ),
                                dcc.Link(
                                    html.Button(
                                        "Buy/Sell Trend",
                                        id="bstrends",
                                        n_clicks=0,
                                        style={
                                            "padding": "10px",
                                            "borderRadius": "5px",
                                            "backgroundColor": "#3a3a3a",
                                            "color": "white",
                                            "fontSize": "14px",
                                        },
                                    ),
                                    href='/bstrend'
                                ),
                                dcc.Link(
                                    html.Button(
                                        "Breakpoints",
                                        id="breakpoints",
                                        n_clicks=0,
                                        style={
                                            "padding": "10px",
                                            "borderRadius": "5px",
                                            "backgroundColor": "#3a3a3a",
                                            "color": "white",
                                            "fontSize": "14px",
                                        },
                                    ),
                                    href='/bkpts'
                                ),
                            ],
                        ),
                    ],
                ),
                # Main Content
                html.Div(
                    style={"width": "75%", "padding": "15px", "borderRadius": "10px"},
                    children=[
                        html.Div(
                            style={"display": "grid", "gridTemplateColumns": "repeat(4, 1fr)", "gap": "15px"},
                            children=[
                                html.Div(
                                    style={
                                        "backgroundColor": "#2c2c2c",
                                        "padding": "10px",
                                        "borderRadius": "5px",
                                        "textAlign": "center",
                                    },
                                    children=[
                                        html.H6("Variable 4", style={"marginBottom": "5px", "fontSize": "14px"}),
                                        html.H3("Value", style={"margin": "0", "fontSize": "18px"}),
                                    ],
                                ),
                                html.Div(
                                    style={
                                        "backgroundColor": "#2c2c2c",
                                        "padding": "10px",
                                        "borderRadius": "5px",
                                        "textAlign": "center",
                                    },
                                    children=[
                                        html.H6("Variable 3", style={"marginBottom": "5px", "fontSize": "14px"}),
                                        html.H3("Value", style={"margin": "0", "fontSize": "18px"}),
                                    ],
                                ),
                                html.Div(
                                    style={
                                        "backgroundColor": "#2c2c2c",
                                        "padding": "10px",
                                        "borderRadius": "5px",
                                        "textAlign": "center",
                                    },
                                    children=[
                                        html.H6("Variable", style={"marginBottom": "5px", "fontSize": "14px"}),
                                        html.H3("Value", style={"margin": "0", "fontSize": "18px"}),
                                    ],
                                ),
                                html.Div(
                                    style={
                                        "backgroundColor": "#2c2c2c",
                                        "padding": "10px",
                                        "borderRadius": "5px",
                                        "textAlign": "center",
                                    },
                                    children=[
                                        html.H6("Variable 2", style={"marginBottom": "5px", "fontSize": "14px"}),
                                        html.H3("Value", style={"margin": "0", "fontSize": "18px"}),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            style={"marginTop": "30px"},
                            children=[
                                html.H1(
                                    "Multi-Frame Analysis",
                                    style={
                                        "textAlign": "center",
                                        "marginBottom": "20px",
                                        "fontSize": "20px",
                                    },
                                ),
                                dcc.Loading(
                                    id="loading-indicator",
                                    type="circle",
                                    children=[
                                        dcc.Graph(id="multi_frame_graph", figure=create_placeholder_figure()),
                                    ],
                                    style={"marginTop": "20px"},
                                ),
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
    Output("multi_frame_graph", "figure"),  # Atualiza o gráfico principal
    [
        # Input("multi_frame", "n_clicks"),  # Botão Multi Frame
        # Input("opt2", "n_clicks"),        # Outro botão
        Input("calculate-button2", "n_clicks"),  # Botão Calcular
    ],
    [State("input-stocks", "value")]  # Estado do campo de texto
)
def update_graph( calc_button,ticker_input):#btn1_clicks, btn2_clicks,
    ctx = dash.callback_context
    if not ctx.triggered:
        return create_placeholder_figure()  # Retorna o gráfico padrão se nenhuma interação ocorreu

    # Determinar qual entrada disparou o callback
    triggered_input = ctx.triggered[0]["prop_id"].split(".")[0]

    if triggered_input == "calculate-button2" and ticker_input:
        # Lógica para atualizar o gráfico com base no campo de texto
        for ticker in ticker_input.split(","):  # Suporta múltiplos tickers separados por vírgulas
            ticker = ticker.strip() + ".SA"
            df[ticker] = [analisar_serie_temporal_yahoo(ticker, time) for time in macro_time]

        return px.line(df)  # Gráfico atualizado com os dados fornecidos

    return create_placeholder_figure()  # Retorna o gráfico padrão como fallback



