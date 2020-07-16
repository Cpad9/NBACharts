###########PUT STUFF LIKE
# Bootstrap Components
import dash_bootstrap_components as dbc
# Core Components
import dash_core_components as dcc
import dash_html_components as html


def createTable(df):
    table2 = dbc.Table.from_dataframe(
        df,
        id='table2',
        bordered=True,
        dark=True,
        responsive=True, ###Keeps table within the div
        striped=True,
        )
    return(table2)

button = html.Div(
    [
        dbc.Button("Click me", id="submit-button", className="mr-2"),
        html.Span(id="example-output", style={"vertical-align": "middle"}),
    ]
)


text_input = html.Div(
    [
        dbc.Input(id="player-name", value="Al Horford", type="text"),
        html.Br(),
        html.P(id="output"),
    ]
)
