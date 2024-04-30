import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

def get_layout():
    df = pd.read_csv("AnimeList.csv")

    # Calculate count of each rating
    rating_counts = df['Rating'].value_counts().reset_index()
    rating_counts.columns = ['Rating', 'Count']

    # Create bar plot
    fig = px.bar(rating_counts, x='Rating', y='Count')
    
    # Dictionary of rating descriptions
    rating_descriptions = {
        'PG-13': 'Teens 13 or older',
        'R - 17+': '17+ (violence & profanity)',
        'R+': 'Mild Nudity',
        'G': 'All Ages',
        'PG': 'Children'
    }

    # Generate HTML elements for each rating description in dictionary
    rating_description_elements = [html.P(f"{rating} - {description}") for rating, description in rating_descriptions.items()]

    layout = html.Div([
        html.H1("Spread of Ratings Across Dataset"),
        html.P("This graph shows the spread of ratings across the dataset."),
        html.Div(rating_description_elements),
        dcc.Graph(figure=fig)
    ])
    
    return layout