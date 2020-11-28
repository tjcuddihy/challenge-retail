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
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Summary"),
                                    html.Br([]),
                                    html.P(
                                        "ACME has experience consistent growth during the period 2004-2006. However, that growth has reverted , with Revenue down ~25%.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Yearly Revenue (w/ YoY % change)"],
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(df_yearly_revenue)),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Yearly Revenue and Gross Profit",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-yearly-performance",
                                        figure=px.bar(
                                            df_yearly_performance,
                                            x="Year",
                                            y="value",
                                            color="variable",
                                            barmode="group",
                                            labels={"value": "$"},
                                            color_discrete_sequence=[
                                                "#519872",
                                                "#34252f",
                                            ],
                                        ),
                                    ),
                                ],
                                className="row",
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 5
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
