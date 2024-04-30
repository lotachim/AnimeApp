import dash
from dash import dcc, html
import base64
import io
import wordcloud
import pandas as pd

df = pd.read_csv("AnimeList.csv")
def get_layout():
    import wordcloud

    # join all genres into a single string (string concatenation)
    all_genres = ' '.join(df['Genres'].str.replace(',', ''))

    # build word cloud
    wordcloud = wordcloud.WordCloud(width=800, height=400, background_color='white').generate(all_genres)

    # Convert the word cloud to image
    img = io.BytesIO()
    wordcloud.to_image().save(img, format='PNG')
    img_str = 'data:image/png;base64,' + base64.b64encode(img.getvalue()).decode()

    layout = html.Div([
        html.H1("WORD CLOUD OF THE MOST FREQUENT GENRES"),
        html.Img(src=img_str, style={'width': '50%', 'height': 'auto'})
    ])
    
    return layout