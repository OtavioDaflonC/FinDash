import dash
from dash import html, dcc

dash.register_page(__name__, path='/', name='Home')

layout = html.Div(
    style={
        'backgroundColor': '#1e1e2f',
        'color': '#ffffff',
        'fontFamily': 'Arial, sans-serif',
        'padding': '2rem',
        'height': '100vh',
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'justifyContent': 'center',
    },
    children=[
        # Logo Section
        html.Div(
            style={
                'marginBottom': '2rem',
            },
            children=html.Img(
                src='../assets/findash_img.png', 
                style={'height': '100px', 'borderRadius': '8px'}
            )
        ),

        # Title Section
        html.H1(
            "Financial Dashboard",
            style={
                'fontSize': '2.5rem',
                'marginBottom': '1rem',
                'fontWeight': 'bold',
                'textAlign': 'center',
            }
        ),

        # Subtitle Section
        html.P(
            "Explore advanced analytics and gain insights into financial data with our secure and intelligent platform.",
            style={
                'fontSize': '1.2rem',
                'marginBottom': '2rem',
                'textAlign': 'center',
                'lineHeight': '1.6',
                'maxWidth': '800px',
            }
        ),

        # Navigation Buttons
        html.Div(
            style={
                'display': 'flex',
                'gap': '1rem',
                'marginTop': '2rem',
            },
            children=[
                dcc.Link(
                    html.Button(
                        "Get Started",
                        style={
                            'backgroundColor': '#007bff',
                            'color': '#ffffff',
                            'padding': '0.8rem 1.5rem',
                            'border': 'none',
                            'borderRadius': '5px',
                            'fontSize': '1rem',
                            'cursor': 'pointer',
                        }
                    ),
                    href='/wallet-simulation'
                ),
                dcc.Link(
                    html.Button(
                        "Learn More",
                        style={
                            'backgroundColor': 'transparent',
                            'color': '#007bff',
                            'padding': '0.8rem 1.5rem',
                            'border': '2px solid #007bff',
                            'borderRadius': '5px',
                            'fontSize': '1rem',
                            'cursor': 'pointer',
                        }
                    ),
                    href='/about'  # Link para uma página de informações
                ),
            ]
        ),
    ]
)
