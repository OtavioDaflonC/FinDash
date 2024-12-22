import plotly.graph_objects as go
import numpy as np


# Gerar arrays predefinidos
grath_xsize = 1000
def generate_random_data(size=1000):
    x = list(range(size))
    y = (np.cumsum(np.random.normal(0, 2, size))**2 +1) /90 # Série estocástica acumulada
    return x, y
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

def create_placeholder_figure():
    # Configurando o layout
    fig = go.Figure(
        layout=go.Layout(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            margin=dict(t=0, b=0, l=0, r=0),
            paper_bgcolor="rgba(0, 0, 0, 0)",  # Fundo transparente
            plot_bgcolor="rgba(0, 0, 0, 0)",  # Fundo transparente do gráfico
        )
    )

    # Adicionando uma anotação central
    fig.add_annotation(
        text="Select all the necessary parameters to generate!",
        x=0.5,
        y=0.5,
        font=dict(size=20, color="gray"),
        showarrow=False,
        xref="paper",
        yref="paper",
    )

    # Adicionando um elemento decorativo (círculo)
    fig.add_shape(
        type="circle",
        x0=0.3,
        y0=0.3,
        x1=0.7,
        y1=0.7,
        xref="paper",
        yref="paper",
        line=dict(color="gray", dash="dot"),
    )

    return fig






