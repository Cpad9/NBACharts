import dash
import dash_table
import pandas as pd

# Bootstrap Components
import dash_bootstrap_components as dbc
# Core Components
import dash_core_components as dcc
import dash_html_components as html

# Input/Output
from dash.dependencies import Input, Output, State
#Components File
from dbc_components import *

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
df = pd.read_csv('PlayerGameLogs/Al Horford.csv')

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP]
)

#Create Table with dataframe
table2 = createTable(df)


jumboWithTable = dbc.Jumbotron(
    [
        text_input,
        button,
        table2,
    ],
    className='w-75 mx-auto',
)


app.layout = dbc.Container(
    [
        jumboWithTable,
    ],
    fluid =True,
    
)

@app.callback(
    # Output(component_id='my-div', component_property='children'),
    dash.dependencies.Output(component_id='table2', component_property='children'),
    [dash.dependencies.Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('player-name','value')]
            )

def update_figure(n_clicks, value):
    filtered_df = pd.read_csv(f'PlayerGameLogs/{value}.csv')
    return (createTable(filtered_df))







# app.layout = html.Div([
#     html.Label('Text Input'),
#     dcc.Input(value='MTL', type='text'),

#     dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict('records'),
# )
# ])




if __name__ == '__main__':
    app.run_server(debug=True)