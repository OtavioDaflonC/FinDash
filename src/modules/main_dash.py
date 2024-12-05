import dash
from dash import html, dcc
import plotly.graph_objects as go

# Register Main Page
dash.register_page(
    __name__,
    path="/main",  # main path
    name="Dashboard",
)

# Gráfico de exemplo
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=["01/01/2024", "01/03/2024", "01/05/2024", "01/07/2024", "01/11/2024"],
        y=[0.5, 0.7, 1.2, 2.5, 3.5],
    )
)

# Layout da página principal
layout = html.Div(
    style={"backgroundColor": "#1e1e1e", "color": "#FFFFFF", "fontFamily": "Arial"},
    children=[
        html.Div(
            style={"display": "flex", "padding": "20px", "gap": "20px"},
            children=[
                # Sidebar
                html.Div(
                    style={"width": "20%", "backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "10px"},
                    children=[
                        html.H4("Localities", style={"textAlign": "center"}),
                        dcc.Dropdown(
                            options=[
                                {"label": "Asset1", "value": "asset1"},
                                {"label": "Asset2", "value": "asset2"},
                                {"label": "Asset3", "value": "asset3"},
                            ],
                            placeholder="Select Asset",
                            style={"color": "black"},
                        ),
                        html.Label("Analysis Options"),
                        dcc.Checklist(
                            options=[
                                {"label": "module_opt1", "value": "module_optv1"},
                                {"label": "module_opt2", "value": "module_optv2"},
                            ],
                            value=["multi_frame_page"],
                            style={"color": "white"},
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
                                dcc.Graph(figure=fig),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)
