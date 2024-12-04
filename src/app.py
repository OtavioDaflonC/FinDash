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
                                {"label": "Itabira Britagem", "value": "itabira_britagem"},
                                {"label": "Wash Plant", "value": "wash_plant"},
                                {"label": "Itabira Sinter Feed", "value": "itabira_sinter_feed"},
                                {"label": "Itabira Quartenario", "value": "itabira_quartenario"}
                            ],
                            placeholder="Select location",
                            style={"color": "black"}
                        ),
                        html.Label("Analysis Options"),
                        dcc.Checklist(
                            options=[
                                {"label": "Dynamic", "value": "dynamic"},
                                {"label": "Efficiency/Integrity", "value": "efficiency_integrity"}
                            ],
                            value=["dynamic"],
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
                                        html.H6("BPFI", style={"textAlign": "center"}),
                                        html.H3("0.051", style={"textAlign": "center"})
                                    ]
                                ),
                                html.Div(
                                    style={"backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "5px"},
                                    children=[
                                        html.H6("BSF", style={"textAlign": "center"}),
                                        html.H3("0.009", style={"textAlign": "center"})
                                    ]
                                ),
                                html.Div(
                                    style={"backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "5px"},
                                    children=[
                                        html.H6("Acceleration", style={"textAlign": "center"}),
                                        html.H3("0.392 G", style={"textAlign": "center"})
                                    ]
                                ),
                                html.Div(
                                    style={"backgroundColor": "#2c2c2c", "padding": "10px", "borderRadius": "5px"},
                                    children=[
                                        html.H6("Speed", style={"textAlign": "center"}),
                                        html.H3("11.874 mm/s", style={"textAlign": "center"})
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