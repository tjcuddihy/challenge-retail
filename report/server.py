import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pathlib

from app import app, server
from pages import overview, salesPerformance, additionalData, forecasts, recommendations


# # get relative data folder
# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath("data").resolve()


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