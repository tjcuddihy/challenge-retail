import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from utils import Header, make_dash_table

import pandas as pd
import pathlib
from math import log10 as log

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../data").resolve()


df_performance_profit = pd.read_csv(
    DATA_PATH.joinpath("03_primary/performance_profit.csv")
)

df_quantity_price_relationship = pd.read_csv(
    DATA_PATH.joinpath("03_primary/quantity_price_relationship.csv")
)


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [layout_intro, layout_quadrant, layout_correlation],
                className="sub_page",
            ),
        ],
        className="page",
    )


layout_intro = html.Div(
    [
        dcc.Markdown(
            """
How can we improve profit? In the context of the current exercise we can explore:

1. Increase Revenue
    1. Sell more
    1. Increase `Unit price`
1. Decrease Expenses
    1. Decrease `Unit cost`
1. Increase capital efficiency - Stop buying/holding stock which does not contribute enough to revenue and gross profit.

We'll take a look at changes to `Unit price` and `Unit cost`, and the implications, later but first let's explore increasing revenue and capital efficiency.
"""
        ),
    ],
    className="row",
)

layout_quadrant = html.Div(
    [
        html.Div(
            [
                html.H5(
                    "Product Quadrant",
                    className="subtitle padded",
                ),
                html.Div(
                    [
                        dcc.Markdown(
                            """
The following section will first derive `Gross margin` as `Gross profit` / `Revenue` and then plot `Product type` (individual products make for a very busy graph) across multiple axes to identify 4 quadrants:

1. Stars - High `Quanitity`, High `Gross margin`, High `Unit price`
    - These are the money makers.
1. Efficiency targets - High `Quanitity`, Low `Gross margin`
    - These product types have great volume sold, so working on gross margin can help turn them into Stars.
1. Marketing targets - Low `Quanitity`, High `Gross margin`
    - These products have good margin but we need to up their `Quantity`; Investing some marketing spend into this category could help push them up into Star territory.
1. Simplification targets - Low `Quanitity`, Low `Gross margin` 
    - These products are candidates to remove from the catalogue: Use the capital for something more effective.

Our first graph is complex; Interpretation as follows:

- Each colour is a `Product type`
- Within each colour, each dot is a `Retailer country`
- The size of the dot is the sale price, AKA `Unit price`
- The x-axis is `Gross margin`
- The y-axis is log(`Quantity`)
- The stop/start controls allow the graph to display the above for each year. Mainly of focus for us will be 2006/2007

In an ideal world, everything would be big dots in the top right quadrant -> High margin, high quantity and high sale price. However, our world isn't that neat so let's make some compromises and see if we can identify some rough quadrants. Skip to the next graph for some ideas.
"""
                        ),
                    ],
                    className="row",
                ),
                dcc.Graph(
                    figure=px.scatter(
                        df_performance_profit.dropna(),
                        x="gross_margin",
                        y="Quantity",
                        color="Product type",
                        size="Unit price",
                        title="Gross Margin V Quantity V Unit price per Product Type",
                        hover_data={
                            "Quantity": ":,",
                            "Retailer country": True,
                            "Unit price": True,
                            "Revenue": True,
                        },
                        animation_frame="Year",
                        animation_group="Retailer country",
                    ).update_yaxes(type="log"),
                ),
            ],
            className="row",
        ),
        html.Div(
            [
                dcc.Graph(
                    figure=px.scatter(
                        df_performance_profit.dropna(),
                        x="gross_margin",
                        y="Quantity",
                        color="Product type",
                        size="Unit price",
                        title="Quadrant plot - Gross Margin V Quantity V Unit price per Product Type",
                        hover_data={
                            "Quantity": ":,",
                            "Retailer country": True,
                            "Unit price": True,
                            "Revenue": True,
                        },
                        animation_frame="Year",
                        animation_group="Retailer country",
                    )
                    .update_yaxes(type="log")
                    .add_hline(y=10000)
                    .add_vline(x=0.45)
                    .add_annotation(
                        x=0.6,
                        y=log(900000),
                        text="Stars",
                        showarrow=False,
                        bgcolor="#ff7f0e",
                    )
                    .add_annotation(
                        x=0.37,
                        y=log(900000),
                        text="Efficiency Targets",
                        showarrow=False,
                        bgcolor="#ff7f0e",
                    )
                    .add_annotation(
                        x=0.6,
                        y=log(1000),
                        text="Marketing Targets",
                        showarrow=False,
                        bgcolor="#ff7f0e",
                    )
                    .add_annotation(
                        x=0.37,
                        y=log(1000),
                        text="Simplification Targets",
                        showarrow=False,
                        bgcolor="#ff7f0e",
                    )
                ),
                dcc.Markdown(
                    """
The values chosen need refinement through business context and collaboration, however, it provides some coarse guidance to our Campling Supply store for heading into 2008 with a plan.
"""
                ),
                html.H5(
                    "Relationship between demand and price", className="subtitle padded"
                ),
                dcc.Markdown(
                    """
Next, let's explore and discuss the impact of changing gross margin, either through decreases to `Unit cost` or increases to `Unit price`. Changing these can potentially have an impact on consumer behaviour and hence Quantity sold. Think back to the last time you had a favourite product which kept the same price but started offering inferior quality... It's a delicate dance to perform and recommendations are far outside the scope of this data and analysis.
However, let's see if we can identify previous times that the business has changed these values and what the effects were.

For the following plot:

- y-axis is the correlation between `Quantity` and `Unit price` over the 4 years
- x-axis is the slope of an least squares regression across `Unit price` for the 4 years (Scaled to [-1,1] for ease of viewing)
- Each colour is a different `Product`, with the dots representing the different `Retailer countries`

The value of the dot on the x-axis shows how the trend for `Unit price` has changed over time. A high positive value indicates that have been price hikes, and a negative value indicates price reductions. The y-axis shows the correlation between this change in `Unit price` and any changes in `Quantity`. If increases to `Unit price` led to decreases in `Quantity` you would expect to see dots in the bottom right corner (increasing slope with negative correlation).
                    """
                ),
            ],
            className="row",
        ),
    ],
    className="row",
)

layout_correlation = html.Div(
    [
        dcc.Graph(
            figure=px.scatter(
                df_quantity_price_relationship,
                y="correlation",
                x="slope",
                color="Product",
                hover_data={"Retailer country": True},
            )
        ),
        dcc.Markdown(
            """
It doesn't appear that the Camping Supply store is having lots of occurences of loss of business due to price hikes. However, they have obviously not been having large increases to their `Unit price` values so they may not yet be testing the limit of their customer's patience.

If I had more time, I'd re-do this analysis to additionally look at changes in `Unit cost`. Also, I would explore the hypothesis from a different angle: I'd plot the YoY changes for `Quantity` and `Unit cost/price` across 2 axes instead of doing correlation and OLS slope stuff. I did it the hard way here `¯\_(ツ)_/¯`
        """
        ),
    ],
    className="row",
)
