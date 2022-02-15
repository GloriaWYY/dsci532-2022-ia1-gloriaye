from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data


# Read in global data
movies = data.movies()

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

server = app.server

app.layout = html.Div([
    html.H2('Welcome to DSCI532 Individual Assignment 1 from Gloria :)'),
    html.Iframe(
        id='histogram',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='IMDB_Rating',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in ["US_Gross", "Worldwide_Gross", "Production_Budget", "IMDB_Rating", "IMDB_Votes"]])])

# Set up callbacks/backend
@app.callback(
    Output('histogram', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(movies).mark_bar().encode(
        x=alt.X(xcol, bin=True),
        y='count()',
        tooltip='count()').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True, port=2022)