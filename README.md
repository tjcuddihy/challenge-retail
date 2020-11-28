# The retail challenge report

## Context

This repo is a clone of the [retail challenge by Eliiza](https://github.com/eliiza/challenge-retail). 

The challenge, suggested to take 3 hours, is as follows:

You have a file `Retail.csv` describing sales data for a hypothetical Camping Supplies store.
Using your tool of choice, answer the following questions:

1. Construct a report breaking down sales by country, sales channel, product and year. The report should be easy to navigate.

2. Provide a list of recommendations for improving the store's profit.

3. Predict the next year of sales for each country. Your predictions will be analysed by a statistically sophisticated manager.

4. What additional data would you want to collect? What analyses would it empower you to run? 

## Evaluating the challenge

First step is to view the notebook `report/3-hour.ipynb`. This is my attempt to answer the questions within the suggested time frame.

```
$ git clone https://github.com/tjcuddihy/challenge-retail.git
$ cd challenge-retail
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r report/requirements.txt
$ jupyter labextension install jupyterlab-plotly@4.13.0
$ jupyter-lab
```

Next is to check out the interactive Dash report. I made this as a way to, hopefully, wow you!

```
$ cd report
$ python server.py
```

## Heroku deployment
If you'd like to deploy the Dash report to Heroku, do the following:

First, make a [heroku account](https://www.heroku.com).
Then on the CLI (in the root dir of `challenge-retail`):
```
$ heroku login
$ heroku create challenge-retail
$ git subtree push --prefix report heroku master
$ heroku ps:scale web=1
```

Check out [here](https://dash.plotly.com/deployment) for more details on deploying Dash apps to Heroku.