import dash_core_components as dcc
import dash_html_components as html

# import plotly.graph_objs as go
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
df_performance_country = pd.read_csv(
    DATA_PATH.joinpath("03_primary/performance_country.csv")
)
df_performance_channel = pd.read_csv(
    DATA_PATH.joinpath("03_primary/performance_channel.csv")
)
df_performance_country_channel = pd.read_csv(
    DATA_PATH.joinpath("03_primary/performance_country_channel.csv")
)
df_performance_line = pd.read_csv(DATA_PATH.joinpath("03_primary/performance_line.csv"))
df_performance_product = pd.read_csv(
    DATA_PATH.joinpath("03_primary/performance_product.csv")
)
df_performance_type = pd.read_csv(DATA_PATH.joinpath("03_primary/performance_type.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    layout_country,
                    layout_channel,
                    layout_product_line,
                    layout_product_type,
                    layout_product,
                    layout_remarks,
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )


layout_country = html.Div(
    [
        html.Div(
            [
                html.H5(
                    "Sales performance by Country",
                    className="subtitle padded",
                ),
                dcc.Graph(
                    figure=px.line(
                        df_performance_country,
                        x="Year",
                        y="Gross profit",
                        color="Retailer country",
                        title="Gross Profit per Country",
                    ).update_xaxes(type="category"),
                    # style={
                    #     "width": "75%",
                    #     "display": "inline-block",
                    # },
                ),
                html.P(
                    "Above we can see that Gross Profit is down across the board for 2007. The following chart shows the YoY % change for each country"
                ),
            ],
            className="row",
        ),
        html.Div(
            [
                dcc.Graph(
                    figure=px.line(
                        df_performance_country[df_performance_country["Year"] != 2004],
                        x="Year",
                        y="Gross profit yoy%",
                        color="Retailer country",
                        title="Gross Profit %YoY per Country",
                        hover_data={
                            "Gross profit yoy%": ":.2%",
                            "Gross profit": ":,.0f",
                        },
                        labels={"Gross profit yoy%": "% Change"},
                    )
                    .update_xaxes(type="category")
                    .update_yaxes(tickformat=",.0%")
                    .add_hline(y=0, line_dash="dot")
                ),
                html.P(
                    """The drop for 2007 ranges from -13.90% for Sweden, to -39.68% in Denmark.
                        That the drop is consistent for all countries indicates that the cause is systemic. It could be either external, e.g. competition or global consumer confidence, or internal, e.g. poor customer service, loss of popular product line etc.
                        """
                ),
                html.P(
                    """Let's look at sales channel performance to see if this sheds light on any issues with customer interactions.
                                """
                ),
            ],
            className="row",
        ),
    ],
    className="row",
)


layout_channel = html.Div(
    [
        html.Div(
            [
                html.H5(
                    "Sales performance by sales channel", className="subtitle padded"
                ),
                dcc.Graph(
                    figure=px.line(
                        df_performance_channel,
                        x="Year",
                        y="Gross profit",
                        color="Order method type",
                        title="Order method type - Log Scale",
                    )
                    .update_xaxes(type="category")
                    .update_yaxes(type="log")
                ),
                html.P(
                    "Web sales dominate for our Camping supplies store and they have dropped substantially. The following chart shows the yoy% changes."
                ),
            ],
            className="row",
        ),
        html.Div(
            [
                dcc.Graph(
                    figure=px.line(
                        df_performance_channel[df_performance_channel["Year"] != 2004],
                        x="Year",
                        y="Gross profit yoy%",
                        color="Order method type",
                        title="Gross Profit %YoY per Order method type",
                        hover_data={
                            "Gross profit yoy%": ":.2%",
                            "Gross profit": ":,.0f",
                        },
                        labels={"Gross profit yoy%": "% Change"},
                    )
                    .update_xaxes(type="category")
                    .update_yaxes(tickformat=",.0%")
                    .add_hline(y=0, line_dash="dot")
                ),
                html.P(
                    "Again, drops across the board except for 'Special' which is very low volume. Let's facet Country performance across Channel."
                ),
            ],
            className="row",
        ),
        html.Div(
            [
                dcc.Graph(
                    figure=px.line(
                        df_performance_country_channel,
                        x="Year",
                        y="Gross profit",
                        color="Retailer country",
                        title="Gross Profit per Country by Channel",
                        hover_data={"Gross profit": ":,.0f"},
                        facet_row="Order method type",
                        height=1000,
                    )
                    .update_xaxes(type="category")
                    .update_yaxes(matches=None)
                    .for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
                ),
                dcc.Markdown(
                    """
Not too much here to help solve our downturn challenge.

Some elements of note (Remember to double click a country name in the legend to focus in on it, then add countries back in one by one to compare):
- Spaniards are increasingly using fax in 2007
- USA, Japan and France are seeing decent gains in Sales Visits for 2007

Let's see if anything interesting is happening across products, lines and type.
                """
                ),
            ],
            className="row",
        ),
    ],
    className="row",
)

layout_product_line = html.Div(
    [
        html.Div(
            [
                html.H5(
                    "Sales performance by Product Line",
                    className="subtitle padded",
                ),
                dcc.Graph(
                    figure=px.line(
                        df_performance_line,
                        x="Year",
                        y="Gross profit",
                        color="Product line",
                        title="Gross Profit per Product line",
                        hover_data={"Quantity": ":,"},
                    ).update_xaxes(type="category")
                ),
                html.P(
                    "Our decreasing performance is across all product lines. The following %YoY graph further highlighting as such."
                ),
            ],
            className="row",
        ),
        html.Div(
            [
                dcc.Graph(
                    figure=px.line(
                        df_performance_line[df_performance_line.Year != 2004],
                        x="Year",
                        y="Gross profit yoy%",
                        color="Product line",
                        title="Gross Profit %YoY per Product line",
                        hover_data={
                            "Gross profit yoy%": ":.2%",
                            "Gross profit": ":,.0f",
                            "Quantity": ":,",
                        },
                        labels={"Gross profit yoy%": "% Change"},
                    )
                    .update_xaxes(type="category")
                    .update_yaxes(tickformat=",.0%")
                    .add_hline(y=0, line_dash="dot")
                ),
            ]
        ),
    ],
    className="row",
)

layout_product_type = html.Div(
    [
        html.Div(
            [
                html.H5(
                    "Sales performance by Product Type",
                    className="subtitle padded",
                ),
                dcc.Graph(
                    figure=px.line(
                        df_performance_type,
                        x="Year",
                        y="Gross profit",
                        color="Product type",
                        title="Gross Profit per Product Type",
                        hover_data={"Quantity": ":,"},
                    ).update_xaxes(type="category")
                ),
                html.P("Watches and Eyeware are the big money makers."),
            ],
            className="row",
        ),
        html.Div(
            [
                dcc.Graph(
                    figure=px.line(
                        df_performance_type[df_performance_type.Year != 2004],
                        x="Year",
                        y="Gross profit yoy%",
                        color="Product type",
                        title="Gross Profit %YoY per Product type",
                        hover_data={
                            "Gross profit yoy%": ":.2%",
                            "Gross profit": ":,.0f",
                            "Quantity": ":,",
                        },
                        labels={"Gross profit yoy%": "% Change"},
                    )
                    .update_xaxes(type="category")
                    .update_yaxes(tickformat=",.0%")
                    .add_hline(y=0, line_dash="dot")
                ),
                html.P(
                    "Looks like climbing equipment is the best Product type showing the smallest %YoY drop for 2007, -1.15%, and $15M Gross profit."
                ),
            ]
        ),
    ],
    className="row",
)

layout_product = html.Div(
    [
        html.Div(
            [
                html.H5(
                    "Sales performance by Product",
                    className="subtitle padded",
                ),
                dcc.Graph(
                    figure=px.line(
                        df_performance_product,
                        x="Year",
                        y="Gross profit",
                        color="Product",
                        title="Gross Profit per Product",
                        hover_data={"Quantity": ":,"},
                    ).update_xaxes(type="category")
                ),
            ],
            className="row",
        ),
        html.Div(
            [
                dcc.Graph(
                    figure=px.line(
                        df_performance_product[df_performance_product.Year != 2004],
                        x="Year",
                        y="Gross profit yoy%",
                        color="Product",
                        title="Gross Profit %YoY per Product",
                        hover_data={
                            "Gross profit yoy%": ":.2%",
                            "Gross profit": ":,.0f",
                            "Quantity": ":,",
                        },
                        labels={"Gross profit yoy%": "% Change"},
                    )
                    .update_xaxes(type="category")
                    .update_yaxes(tickformat=",.0%")
                    .add_hline(y=0, line_dash="dot")
                ),
                html.P(
                    "Zooming into 2007 around the 0% YoY mark, there are a few successful products:"
                ),
                html.Ul(
                    [
                        html.Li(
                            "Capri: 93.3% Gross profit increase 2006-2007, \$4.58M Gross profit"
                        ),
                        html.Li("Cat Eye: 27.9% YoY growth, \$8.54M Gross profit"),
                        html.Li("Sam (A watch): 27.56% growth, \$4.66M profit"),
                    ]
                ),
            ]
        ),
    ],
    className="row",
)

layout_remarks = html.Div(
    [
        html.H5("Remarks", className="subtitle padded"),
        html.P(
            "Across the board business is down for 2007. There a couple of products and channels that are performing well but not enough to offset the huge drop in business in the `United States` market. Next up we'll investigate ideas for picking up profit for 2008!"
        ),
    ],
    className="row",
)
