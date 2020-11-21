import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(src=app.get_asset_url("tent.svg"), className="logo",),
                    html.A(
                        html.Button("Learn More", id="learn-more-button"),
                        href="https://www.linkedin.com/in/thomas-cuddihy/",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("ACME Camping Performance")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/retail-challenge/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview", href="/retail-challenge/overview", className="tab first",
            ),
            dcc.Link(
                "Sales Performance",
                href="/retail-challenge/sales-performance",
                className="tab",
            ),
            dcc.Link(
                "Recommendations",
                href="/retail-challenge/recommendations",
                className="tab",
            ),
            dcc.Link("Forecasts", href="/retail-challenge/forecasts", className="tab",),
            dcc.Link(
                "Additional data",
                href="/retail-challenge/additional-data",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
