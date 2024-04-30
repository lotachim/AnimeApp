import dash
from dash import dcc, html
app = dash.Dash(__name__)
# data overview
data_overview = (
    "The dataset used for this Dash App contains information about Anime Ratings.\n"
    "Anime refers to Japanese animation television series.\n"
    "The dataset contains 162 rows and 6 columns.\n"
    "The dataset was gotten from an already existing dataset on Kaggle.\n"
    "Data Cleaning techniques were carried out on the original dataset.\n"
    "The required Columns for this project where then merged into this dataset.\n"
)

def get_layout():
    layout = html.Div([
        html.H1("Welcome to Anime Ratings Dashboard"),
        html.P("This dashboard provides insights into anime ratings data."),
        html.P("Navigate through the tabs to explore different visualizations."),
        html.P("Dataset Overview:"),
        html.P(data_overview)  # Display the dataset overview text

    ])

    return layout