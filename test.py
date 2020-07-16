import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [dcc.Location(id="url"), html.Div(id="content")], className="p-5"
)

table = dbc.Table(
    [
        html.Thead([html.Td("Name"), html.Td("Link")]),
        html.Tr(
            [
                html.Td("Page 1"),
                html.Td(dcc.Link("page 1 link", href="/page-1")),
            ]
        ),
        html.Tr(
            [
                html.Td("Page 2"),
                html.Td(dcc.Link("page 2 link", href="/page-2")),
            ]
        ),
    ],
    bordered=True,
)

page1 = html.Div([html.P("This is page 1"), dcc.Link("return home", href="/")])
page2 = html.Div([html.P("This is page 2"), dcc.Link("return home", href="/")])


@app.callback(Output("content", "children"), [Input("url", "pathname")])
def populate_page(pathname):
    if pathname == "/":
        return table
    elif pathname == "/page-1":
        return page1
    elif pathname == "/page-2":
        return page2
    return "404 - not recognised"


if __name__ == "__main__":
    app.run_server(debug=True)


# app.layout = html.Div([
#     html.Div(dcc.Input(id='player-name', value='Al Horford', type='text')),
#     html.Button('Submit', id='submit-button', n_clicks=0,),
#     html.Div(id='my-div'),
    
#     ####My TaBLE
#     # dash_table.DataTable(
#     #     id='table',
#     #     columns=[{"name": i, "id": i} for i in df.columns],
#     #     data=df.to_dict('records'),
#     #     # Bootstrap
#     # ),

#     ####Doing Boostrap Component Stuff
#     dbc.Input(id="input", placeholder="Sup",type="text"),
#     # table,
#     table2,

#     # html.Div(id='test-div'(table)),
    
# ])