import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
# style = 
app = Dash(__name__, pages_folder='pages',use_pages=True)#external_stylesheets=style

# Layout do dashboard
app.layout = html.Div(
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
                                {"label": "Asset3", "value": "asset3"}
                                
                            ],
                            placeholder="Select Asset",
                            style={"color": "black"}
                        ),
                        html.Label("Analysis Options"),
                        dcc.Checklist(
                            options=[
                                {"label": "module_opt1", "value": "module_optv1"},
                                {"label": "module_opt2", "value": "module_optv2"}
                            ],
                            value=["multi_frame_page"],
                            style={"color": "white"}
                        )
                    ]
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
                                        html.H3("value", style={"textAlign": "center"})
                                    ]
                                ),
                                html.Div(
                                    style={"backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "5px"},
                                    children=[
                                        html.H6("variable3", style={"textAlign": "center"}),
                                        html.H3("value", style={"textAlign": "center"})
                                    ]
                                ),
                                html.Div(
                                    style={"backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "5px"},
                                    children=[
                                        html.H6("variable", style={"textAlign": "center"}),
                                        html.H3("value", style={"textAlign": "center"})
                                    ]
                                ),
                                html.Div(
                                    style={"backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "5px"},
                                    children=[
                                        html.H6("variable2", style={"textAlign": "center"}),
                                        html.H3("value", style={"textAlign": "center"})
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            style={"marginTop": "20px"},
                            children=[
                                dcc.Graph(figure=fig)
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)