# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import pathlib
import plotly.express as px
from pages import overview, salesPerformance, additionalData, forecasts, recommendations


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()


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


########
# Set up the app
########
app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/retail-challenge/sales-performance":
        return salesPerformance.create_layout(app)
    elif pathname == "/retail-challenge/recommendations":
        return recommendations.create_layout(app)
    elif pathname == "/retail-challenge/forecasts":
        return forecasts.create_layout(app)
    elif pathname == "/retail-challenge/additional-data":
        return additionalData.create_layout(app)
    elif pathname == "/retail-challenge/full-view":
        return (
            overview.create_layout(app),
            salesPerformance.create_layout(app),
            recommendations.create_layout(app),
            forecasts.create_layout(app),
            additionalData.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
