import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_revenue = pd.read_csv(DATA_PATH.joinpath("03_primary/revenue.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [layout_intro, layout_forecast],
                className="sub_page",
            ),
        ],
        className="page",
    )


layout_intro = html.Div(
    [
        html.H5("Sales forecasts for 2008"),
        dcc.Markdown(
            """
Time series prediction with such a small data set (4 obs per level of prediction) is going to be very rough and inaccurate. However, it's _technically_ possible to do a simple regression with 3 observations... So let's give it a go!

Also, check out [Rob Hyndman](https://robjhyndman.com) for all things time series, especially [this treatise](https://robjhyndman.com/papers/shortseasonal.pdf) on forecasting with small sample size.
"""
        ),
    ],
    className="row",
)

layout_forecast = html.Div(
    [
        dcc.Graph(
            figure=px.line(
                df_revenue,
                x="Year",
                y="Revenue",
                color="Retailer country",
                title="Revenue forecast per country",
            )
            .add_vrect(
                x0=2007.80,
                x1=2008.20,
                annotation_text="Forcast",
                annotation_position="top left",
                fillcolor="green",
                opacity=0.15,
                line_width=0,
            )
            .update_traces(mode="markers+lines")
        ),
        dcc.Markdown(
            """
So we have generated some predictions but I'd like to briefly come back to the difficulty in forecasting short time series:
> Is the drop from '06 to '07 a change in the trend? Or is it a noisy blip on the radar? 

There is noway to tell, but the uncertainty, as a proportion of the total sample size, is massive and so makes this a guessing game. (See Q4 for a recommendation)

With the data we have, we may be better served by using simple mean/median and not trying to use a linear model, or a seasonal time series model.
        """
        ),
    ],
    className="row",
)