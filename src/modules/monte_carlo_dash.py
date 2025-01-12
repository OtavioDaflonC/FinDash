import dash
import pandas as pd
from dash import html, dcc, Input, Output, State, ctx,MATCH, ALL
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from modules.monte_carlo import monte_carlo_pred, monte_carlo_retro, description
from utils import *


dash.register_page(
    __name__,
    path='/mtcarlo', 
    name="Monte Carlo Dashboard",
)




