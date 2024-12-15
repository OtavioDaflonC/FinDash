import dash
import sys
import os

import pandas as pd
from dash import html, dcc, Input, Output, State
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from utils import *
sys.path.append(os.path.abspath("src"))


# Configuração do Dash com suporte para múltiplas páginas
app = dash.Dash(__name__, pages_folder="modules", use_pages=True,suppress_callback_exceptions=True)#

# Layout 
app.layout = html.Div(
    style={"backgroundColor": "#1e1e1e", "color": "#FFFFFF", "fontFamily": "Arial"},
    children=[
        dash.page_container,  # Renderiza apenas a página atual
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)