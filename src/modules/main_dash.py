import dash
import pandas as pd
from dash import html, dcc, Input, Output, State, ctx,MATCH, ALL
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from modules.wallet_simulation import wallet_simulate, asset
from utils import *

#=========================================================================
# for example:

start = '2018-01-01'
ativos = {
    'BBAS3.SA': [ 0.209],  
    'CSNA3.SA': [ 0.042],  
    'FLRY3.SA': [  0.051],
    'ITSA4.SA': [ 0.089],
    'KEPL3.SA': [ 0.175],
    'KLBN4.SA': [ 0.083],
    'TAEE4.SA': [ 0.061],
    'MGLU3.SA': [ 0.002],
    'UNIP6.SA': [ 0.107],
    'GOAU4.SA': [ 0.18],
 
}

indices = ['^GSPC', '^BVSP','^N225']  
data_comparacao = (start, '2024-11-20') # datas de compra precisam ser antes da primeira data desse intervalo


#end example
#============================================================================

dash.register_page(
    __name__,
    path="/wallet-simulation",  # main path
    name="Dashboard",
)



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
                            "Select Assets",
                            style={"textAlign": "center", "marginBottom": "20px", "fontSize": "18px"},
                        ),
                        dcc.Store(id="stored-stocks-data"),
                        dcc.Input(
                            id="dropdown-stocks",
                            type='text',
                            placeholder="Add a stock to the list",
                            style={
                                "width": "100%",
                                "padding": "10px",
                                "marginBottom": "10px",
                                "borderRadius": "5px",
                                "border": "1px solid #ccc",
                            },
                        ),
                        dcc.Input(
                            id="input-percentage",
                            type="number",
                            placeholder="Add the weight of the stock in wallet (%)",
                            min=0,
                            max=100,
                            style={
                                "width": "100%",
                                "padding": "10px",
                                "marginBottom": "10px",
                                "borderRadius": "5px",
                                "border": "1px solid #ccc",
                            },
                        ),
                        html.Button(
                            "Adicionar Ativo",
                            id="add-stock-button",
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
                        html.Div(
                            id="stocks-list",
                            style={"marginTop": "20px", "color": "#FFFFFF"},
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
                        # Botões em vez de divs horizontais
                        html.Div(
                            style={
                                "display": "grid",
                                "gridTemplateColumns": "repeat(4, 1fr)",
                                "gap": "15px",
                            },
                            children=[
                            html.Div(
                                style={
                                    "display": "flex",
                                    "justifyContent": "center",
                                    "alignItems": "center",
                                    "borderRadius": "8px",
                                    "backgroundColor": "#2c2c2c",
                                    "padding": "20px",
                                    "color": "white",
                                    "fontSize": "18px",
                                    "width": "1050px",  # Somando as larguras dos botões (4 * 262px) com gaps mínimos
                                    "height": "105px",  # Igual à altura dos botões
                                    "textAlign": "center",
                                },
                                children=[
                                    html.P(
                                        "Texto instrutivo aqui. Substitua este texto pelo conteúdo necessário.",
                                        style={
                                            "margin": "0",
                                            "fontSize": "18px",
                                            "fontWeight": "bold",
                                            "textAlign": "center",
                                        },
                                    ),
                                ],
                            )
                            ],
                        ),
                        html.Div(
                            style={"marginTop": "30px"},
                            children=[
                                html.H1(
                                    "Wallet Simulation",
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
                                        dcc.Graph(id="main-graph", figure=create_placeholder_figure()),
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

# @dash.callback(
#     Output("header-animation", "figure"),
#     Input("interval-update", "n_intervals"),
# )
# def update_header_animation(n_intervals):
#     # Limitar o índice ao tamanho dos dados
#     index = min(n_intervals + 1, len(predefined_x))
#     return create_fig_with_point(index)


@dash.callback(
    [
        Output("main-graph", "figure"),  # Atualiza o gráfico principal
        Output("stocks-list", "children"),  # Atualiza a lista de ativos exibida
    ],
    [
        Input("add-stock-button", "n_clicks"),  # Botão "Adicionar Ativo"
        Input({"type": "remove-button", "index": ALL}, "n_clicks"),  # Botões de remoção
    ],
    [
        State("dropdown-stocks", "value"),  # Valor selecionado no dropdown
        State("input-percentage", "value"),  # Porcentagem digitada
        State("stocks-list", "children"),  # Lista de ativos atual
    ],
    prevent_initial_call=True,
)
def manage_stocks(add_clicks, remove_clicks, stock, percentage, current_list):
    # Inicializar lista, se necessário
    if current_list is None:
        current_list = []

    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]  # Identifica o elemento que acionou o callback

    # Se o botão de adicionar foi clicado
    if triggered_id == "add-stock-button":
        if not stock or not percentage:  # Validação dos inputs
            return create_placeholder_figure(), current_list

        # Gerar ID único baseado no nome do ativo (ou outra lógica de identificação única)
        item_id = f"{stock}-{percentage}-{len(current_list)}"

        # Criar novo item para a lista
        new_item = html.Div(
            id={"type": "stock-item", "index": item_id},  # ID único para cada seção
            style={"display": "flex", "justifyContent": "space-between", "padding": "5px 0"},
            children=[
                html.Span(f"{stock} ({percentage}%)", style={"color": "#FFFFFF"}),
                html.Button(
                    "Remove",
                    id={"type": "remove-button", "index": item_id},  # ID único dinâmico
                    n_clicks=0,
                    style={
                        "backgroundColor": "red",
                        "color": "white",
                        "border": "none",
                        "borderRadius": "5px",
                        "padding": "5px",
                        "cursor": "pointer",
                        "fontSize": "12px",
                    },
                ),
            ],
        )
        # Atualiza a lista de componentes
        updated_list = current_list + [new_item]

        # Simular cálculo de gráfico
        asset[stock + ".SA"] = [round(percentage / 100, 2)]
        result = wallet_simulate(
            asset, indices=["^BVSP", "^GSPC", "BTC-USD"], data_comparacao=("2018-01-01", "2024-11-20")
        )

        if isinstance(result, go.Figure):
            figure = result
        else:
            figure = create_placeholder_figure()

        return figure, updated_list

    # Se um botão de remoção foi clicado
    elif "remove-button" in triggered_id:
        # Identificar o ID do botão clicado
        remove_id = eval(triggered_id)["index"]  # Obtem o ID único do botão clicado

        # Remover o item correspondente ao ID
        updated_list = [
            item for item in current_list if item["props"]["id"]["index"] != remove_id
        ]

        # Recalcular o gráfico (se necessário) com a nova lista
        figure = create_placeholder_figure()  # Ajuste para recalcular o gráfico, se for o caso
        return figure, updated_list

    return create_placeholder_figure(), current_list  # Caso nada seja acionado



