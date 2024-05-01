import dash
from dash import dcc, html, Input, Output
import landingpage
import scatterplot
import page3
import wordcloudpage
import plotly.express as px
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='nav-banner'),
    html.Div(id='page-content')
])

# Callback to display the page content
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    try:
        if pathname == '/scatter-plot':
            return scatterplot.get_layout() 
        elif pathname == '/ratings-spread':
            return page3.get_layout()
        elif pathname == '/wordcloud':
            return wordcloudpage.get_layout()
        else:
            return landingpage.get_layout()
    except Exception as e:
        return html.Div([
            html.H1("500: Internal Server Error"),
            html.P(str(e))
        ])

# Callback to generate the navigation banner
@app.callback(Output('nav-banner', 'children'),
              [Input('url', 'pathname')])
def generate_nav_banner(pathname):
    return html.Div([
        html.H3("Navigation Banner"),
        html.Nav([
            html.Ul([
                html.Li(html.A("Landing Page", href="/")),
                html.Li(html.A("Scatter Plot", href="/scatter-plot")),
                html.Li(html.A("Ratings Spread", href="/ratings-spread")),
                html.Li(html.A("Word Cloud", href="/wordcloud"))
            ])
        ])
    ])

# Callback to update scatter plot
@app.callback(
    Output('scatter-plot-graph', 'figure'),
    [Input('studio-dropdown', 'value')]
)
def update_scatter_plot(selected_studio):
    filtered_df = scatterplot.df if selected_studio == 'All Studios' else scatterplot.df[scatterplot.df['Studios'] == selected_studio]
    fig = px.scatter(filtered_df, x='Score', y='Title', hover_data=['Title'], title='Anime Ratings Scatter Plot')
    return fig
if __name__ == '__main__':
    app.run_server(debug=True)
