import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Read data from CSV
df = pd.read_csv("AnimeList.csv")

# Define layout for scatter plot page
def get_layout():
    layout = html.Div([
        html.H1("Anime Ratings Scatter Plot"),
        html.Div([
            dcc.Dropdown(
                id='studio-dropdown',
                options=[{'label': studio, 'value': studio} for studio in df['Studios'].unique()],
                value='All Studios',
                multi=False
            ),
        ], style={'width': '30%', 'display': 'inline-block'}),
        dcc.Graph(id='scatter-plot-graph')
    ])
    return layout
def register_callbacks(app): #Define teh callback function
    @app.callback(
        Output('scatter-plot-graph', 'figure'),
        [Input('studio-dropdown', 'value')]
    )
    def update_scatter_plot(selected_studio): #update the scatterplot when user changes selection
        filtered_df = df if selected_studio == 'All Studios' else df[df['Studios'] == selected_studio]
        fig = px.scatter(filtered_df, x='Score', y='Title', hover_data=['Title'], title='Anime Ratings Scatter Plot')
        return fig