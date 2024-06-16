from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

from navbar import Navbar
from description import Description
from question_card import QuestionCard
from dashboard import Dashboard

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY, dbc.icons.BOOTSTRAP])

app.layout = html.Div([
    Navbar,
    Description,
    QuestionCard,
    html.Div(dbc.Button("Submit Test"), className="mb-4 text-center border"),
    Dashboard,
    html.Div(dbc.Button("Download Report"), className="text-center border")
])

if __name__ == "__main__":
    app.run_server(debug=True)
