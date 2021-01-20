import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
from dash.dependencies import Input, Output
import sys

app = dash.Dash(__name__)

t = np.arange(0, 100, 0.1)
y_1 = np.sin(t)
y_2 = np.cos(t)
patients = [{'label': 'patient1', 'value': '1'},
            {'label': 'patient2', 'value': '2'},
            {'label': 'patient3', 'value': '3'}]

patient = {'birthdate': 'urodziny',
            'disabled': 'alo',
            'firstname': 'firstname',
            'lastname': 'lastname'}

app.layout = html.Div(children=[
    html.H1(children='Orthopedist\'s aplication for movement analysis'),

    html.Hr(),

    dcc.Dropdown(
        id='chose_patient',
        options=patients,
        value='1'
    ),

    html.Hr(),

    html.Div(id='patient_data', children=[
        html.Div(children=[html.B("Birthdate: "), html.Span(id="birthdate")]),
        html.Div(children=[html.B("Disabled: "), html.Span(id="disabled")]),
        html.Div(children=[html.B("Firstname: "), html.Span(id="firstname")]),
        html.Div(children=[html.B("Lastname: "), html.Span(id="lastname")])
    ]),

    html.H3(children='Patient 1, real-time data:'),

    dcc.Graph(
        id='left_right_graph'),
    dcc.RadioItems(
        id='chose_left_right',
        options=[
            {'label': 'Pressure point 1', 'value': '1'},
            {'label': 'Pressure point 2', 'value': '2'},
            {'label': 'Pressure point 3', 'value': '3'}
        ],
        value='1'
    ),

    html.Hr(),

    dcc.Graph(
        id='statistical_graph',
    ),
    dcc.RadioItems(
        id='chose_statstical_data',
        options=[
            {'label': 'Maximal value', 'value': '1'},
            {'label': 'Minimal value', 'value': '2'},
            {'label': 'Mean value', 'value': '3'}
        ],
        value='1'
    ),

    html.Hr(),

    html.Div([
    dcc.Graph(id='time-graph'),
    dcc.Slider(
        id='time-slider',
        min=0,
        max=600,
        step=1
    )
])
])


@app.callback(
    Output(component_id='left_right_graph', component_property='figure'),
    Input(component_id='chose_left_right',  component_property='value'),
    Input(component_id='chose_patient',  component_property='value'))
def update_left_right_graph(pressure_point, patient):
    change = int(pressure_point)
    change2 = int(patient)
    t = np.arange(0, 100, 0.1)
    y_1 = np.sin(t + change + change2)
    y_2 = np.cos(t + change + change2)
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=t,
        y=y_1,
        name="Left foot"
    ))
    fig.add_trace(go.Scatter(
        x=t,
        y=y_2,
        name="Right foot"
    ))
    fig.update_layout(
        yaxis={'range': [-3, 3]},
        xaxis={'range': [0, 100]},
        title='Left-rifght foot comparison',
        xaxis_title="Time",
        yaxis_title="Pressure",
        legend_title="Legend",
    )

    return fig


@app.callback(
    Output(component_id='statistical_graph', component_property='figure'),
    Input(component_id='chose_statstical_data',  component_property='value'),
    Input(component_id='chose_patient',  component_property='value'))
def update_statistical_graph(selected_stat, patient):
    change = int(selected_stat) * 100
    change2 = int(patient) * 100
    y = [1024, 1036, 1072, 965, 1055, 1000]
    y = [x+change+change2 for x in y]
    figure = {
        'data': [{
            'x': ['L0', 'L1', 'L2', 'R0', 'R1', 'R2'],
            'y': y,
            'type': 'bar',
            'name': 'Maximal pressure'
        }],
        'layout': {
            'title': 'Statistical data about foot pressure points',
        }
    }

    return figure

@app.callback(
    Output(component_id='birthdate', component_property='children'),
    Output(component_id='disabled', component_property='children'),
    Output(component_id='firstname', component_property='children'),
    Output(component_id='lastname', component_property='children'),
    Input(component_id='chose_patient',  component_property='value'))
def update_patient(patient_number):
    return list(patient.values())

@app.callback(
    Output('time-graph', 'figure'),
    Input('time-slider', 'value'))
def update_figure(time):
    y = [1024, 1036, 1072, 965, 1055, 1000]
    figure = {
        'data': [{
            'x': ['L0', 'L1', 'L2', 'R0', 'R1', 'R2'],
            'y': y,
            'type': 'bar',
            'name': 'Maximal pressure'
        }],
        'layout': {
            'title': 'Statistical data about foot pressure points',
        }
    }

    return figure

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050, debug=True)
