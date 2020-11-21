import dash_core_components as dcc
import dash_html_components as html

# import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px
from app import app

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../data").resolve()


df_sales_performance = pd.read_csv(
    DATA_PATH.joinpath("03_primary/sales_performance.csv")
)

col_options = [
    dict(label=x, value=x)
    for x in [
        "Product",
        "Order method type",
        "Retailer country",
        "Revenue",
        "Quantity",
        "Gross profit",
    ]
]
dimensions = ["y", "color"]


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
                                    html.H6(
                                        "Yearly Revenue and Gross Profit",
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                [
                                                    d + ":",
                                                    dcc.Dropdown(
                                                        id=d, options=col_options
                                                    ),
                                                ]
                                            )
                                            for d in dimensions
                                        ],
                                        style={"width": "25%", "float": "left"},
                                    ),
                                    dcc.Graph(
                                        id="graph-sales-performance",
                                        style={
                                            "width": "75%",
                                            "display": "inline-block",
                                        },
                                    ),
                                ],
                                className="row",
                            )
                        ],
                        className="row",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )

