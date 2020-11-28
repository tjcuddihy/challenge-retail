import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_yearly_revenue = pd.read_csv(DATA_PATH.joinpath("03_primary/yearly_revenue.csv"))
df_yearly_performance = pd.read_csv(
    DATA_PATH.joinpath("03_primary/yearly_performance.csv")
)
# df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            html.Div(
                [layout_intro, layout_graphs, layout_howto],
                className="sub_page",
            ),
        ],
        className="page",
    )


layout_intro = html.Div(
    [
        html.Div(
            [
                html.H5("Summary"),
                html.Br([]),
                html.P(
                    "ACME has experienced consistent growth during the period 2004-2006. However, that growth has reverted, with Revenue down ~25%.",
                    style={"color": "#ffffff"},
                    className="row",
                ),
                html.P(
                    "This drop has occurred across all Countries, Product Lines and Product Types. Additional data and analysis are required to uncover the cause of the drop and to develop more robust recommendations for change into 2008.",
                    style={"color": "#ffffff"},
                    className="row",
                ),
            ],
            className="product",
        )
    ],
    className="row",
)

layout_graphs = html.Div(
    [
        html.H5(
            ["Yearly Revenue (w/ YoY % change)"],
            className="subtitle padded",
        ),
        html.Div(
            [
                html.Table(make_dash_table(df_yearly_revenue)),
            ],
            className="row",
        ),
        dcc.Graph(
            id="graph-yearly-performance",
            figure=px.bar(
                df_yearly_performance,
                x="Year",
                y="value",
                color="variable",
                barmode="group",
                title="Yearly Revenue and Gross Profit",
                labels={"value": "$"},
            ).update_yaxes(tickprefix="$"),
        ),
    ],
    className="row",
)

layout_howto = html.Div(
    [
        html.H5("How to read this report.", className="subtitle padded"),
        dcc.Markdown(
            """
The code to view and evaluate my report can be found [here](https://github.com/tjcuddihy/challenge-retail), feel free to jump in and explore. 

Within is a `report` folder which contains a notebook, `3-hour.ipynb`. This notebook is where I performed my initial analysis of the data. Admittedly it took longer than the 3-hours but a lot of that was due to learning [Plotly](https://plotly.com/python/). From there, I spent several days learning [Dash](https://plotly.com/dash/) and built this interactive report.

If you'd like to learn more about the Dash code, it's also within that folder. You can even clone the repo and deploy your own version to Heroku (See the toplevel `README.md` for instructions).
    """
        ),
    ]
)
