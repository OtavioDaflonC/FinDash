import dash
import pandas as pd
from dash import html, dcc, Input, Output, State, ctx,MATCH, ALL
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from modules.wallet_simulation import wallet_simulate, asset, description
from utils import *

default_index = ["^BVSP", "^GSPC", "BTC-USD"]


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
        # Date selection
        html.Div(
            style={
                "display": "flex",
                "justifyContent": "center",
                "marginBottom": "20px",
                "padding": "10px 20px",
                "backgroundColor": "#2c2c2c",
                "borderRadius": "10px",
            },
            children=[
                html.Label(
                    "Select time range:",
                    style={"marginRight": "10px", "color": "#FFFFFF", "textAlign": "center"},
                ),
                dcc.DatePickerRange(
                    id="date-picker-range",
                    start_date_placeholder_text="  Start Date",
                    end_date_placeholder_text="  End Date",
                    calendar_orientation="horizontal",
                    day_size=39,
                    display_format="DD/MM/YYYY",
                    style={"backgroundColor": "#1e1e1e", "color": "#FFFFFF", "textAlign": "center"},
                ),
                                html.Button(
            "Confirm",
            id="confirm-date-button",
            n_clicks=0,
            style={
                "marginLeft": "10px",
                "padding": "10px 20px",
                "backgroundColor": "#007BFF",
                "color": "white",
                "border": "none",
                "borderRadius": "5px",
                "cursor": "pointer",
                "fontSize": "14px",
            },
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
                            "Our Playground:",
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
                        # "alignItems": "center",
                        "borderRadius": "8px",
                        "backgroundColor": "#2c2c2c",
                        "padding": "20px",
                        "color": "white",
                        "fontSize": "18px",
                        "width": "1050px",  # Adjust as needed
                        "height": "255px"  # Adjust as needed
                        # "textAlign": "center",
                    },
                    children=[
                        html.P(
                            description, 
                            style={
                                "margin": "0",
                                "fontSize": "18px",
                                # "fontWeight": "bold",
                                #"textAlign": "center",
                                "whiteSpace": "pre-wrap",  # Preserve spaces and line breaks
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


@dash.callback(
    [
        Output("main-graph", "figure"),  # Atualiza o gráfico principal
        Output("stocks-list", "children"),  # Atualiza a lista de ativos exibida
        Output("stored-stocks-data", "data"),  # Atualiza os dados armazenados
    ],
    [
        Input("add-stock-button", "n_clicks"),  # Botão "Adicionar Ativo"
        Input({"type": "remove-button", "index": ALL}, "n_clicks"),  # Botões de remoção
        Input("confirm-date-button", "n_clicks"),  # Botão para confirmar a data
    ],
    [
        State("dropdown-stocks", "value"),  # Valor selecionado no dropdown
        State("input-percentage", "value"),  # Porcentagem digitada
        State("stored-stocks-data", "data"),  # Dados armazenados dos ativos
        State("date-picker-range", "start_date"),  # Data inicial selecionada
        State("date-picker-range", "end_date"),  # Data final selecionada
    ],
    prevent_initial_call=True,
)
def manage_stocks(add_clicks, remove_clicks, confirm_date_clicks, stock, percentage, current_data, start_date, end_date):
    if current_data is None:
        current_data = []
    if stock is None:
        pass
    else:
        stock = stock.upper()
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]  # Identifica o elemento que acionou o callback

    # Adicionar um novo ativo
    if triggered_id == "add-stock-button" and stock and percentage:
        new_item = {"stock": stock, "percentage": percentage}
        current_data.append(new_item)

    # Remover ativos
    elif "remove-button" in triggered_id:
        # Obtem o índice do botão clicado
        remove_indices = [i for i, n in enumerate(remove_clicks) if n > 0]
        if remove_indices:
            index_to_remove = remove_indices[0]
            current_data.pop(index_to_remove)

    # Atualizar o gráfico
    figure = create_placeholder_figure()  # Gráfico padrão
    if current_data:
        # Converte os dados para o formato necessário
        asset_data = {item["stock"]: [round(item["percentage"] / 100, 2)] for item in current_data}
        result = wallet_simulate(
            asset_data, indices=default_index, data_comparacao=(start_date.replace("/", "-"), end_date.replace("/", "-"))
        )
        if isinstance(result, go.Figure):
            figure = result

    # Atualizar a lista de ativos exibida
    updated_list = [
        html.Div(
            id={"type": "stock-item", "index": i},
            style={"display": "flex", "justifyContent": "space-between", "padding": "5px 0"},
            children=[
                html.Span(f"{item['stock']} ({item['percentage']}%)", style={"color": "#FFFFFF"}),
                html.Button(
                    "Remove",
                    id={"type": "remove-button", "index": i},
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
        for i, item in enumerate(current_data)
    ]

    return figure, updated_list, current_data
