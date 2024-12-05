import dash
from dash import html

# Configuração do Dash com suporte para múltiplas páginas
app = dash.Dash(__name__, pages_folder="modules", use_pages=True)

# Layout 
app.layout = html.Div(
    style={"backgroundColor": "#1e1e1e", "color": "#FFFFFF", "fontFamily": "Arial"},
    children=[
        dash.page_container,  # Renderiza apenas a página atual
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)