import plotly.graph_objects as go

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
        text="Selecione um parâmetro para visualizar o gráfico!",
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

