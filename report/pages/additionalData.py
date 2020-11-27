import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../data").resolve()


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [layout_intro],
                className="sub_page",
            ),
        ],
        className="page",
    )


layout_intro = html.Div(
    [
        html.H5("Recommendations for additional data and analysis"),
        dcc.Markdown(
            """
To address forecasting (Q3), I'd ask for finer granularity revenue data so that we have enough observations to develop a seasonal time-series model. I'd be curious to see if we could tease out the ongoing direction of the revenue trend with such data.

To further investigate the causes of the drop, I'd be keen to understand who are the competitors and then investigate the annual reports of any which are publicly traded. That will give some insight to see if the cause is internal or external. Additionally, I'd want to investigate the website's UI/UX to help see if there are changes which could be made, or reversed, to try and get American's back to buying. 

I've gone over time so I'll leave it here.
"""
        ),
    ],
    className="row",
)