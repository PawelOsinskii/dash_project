import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
from dash.dependencies import Input, Output
import sys
import plotly.express as px
import pandas as pd
import requests

API=r'http://127.0.0.1:5000/'

def get_num_of_patients():
    api_link = API + 'patients'
    data = pd.read_json(api_link)
    return len(data)
NUM_OF_PATIENTS = get_num_of_patients()
df = {}
patient = {}
app = dash.Dash(__name__)

patients = []
for el in list(range(1, NUM_OF_PATIENTS+1)):
    patients.append({'label': f'patient {el}', 'value': f'{el}'})




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

    html.Hr(),

    html.H3(children='Patient 1, real-time data:'),

    dcc.Graph(
        id='left_right_graph'),
    dcc.RadioItems(
        id='chose_left_right',
        options=[
            {'label': 'Pressure point 1', 'value': '0'},
            {'label': 'Pressure point 2', 'value': '1'},
            {'label': 'Pressure point 3', 'value': '2'}
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
            step=1,
            value=0
        )
    ]),

    html.Div(id='time-stamp', style={'text-align' : 'center'})
])


@app.callback(
    Output(component_id='left_right_graph', component_property='figure'),
    Input(component_id='chose_left_right',  component_property='value'),
    Input(component_id='chose_patient',  component_property='value'))
def update_left_right_graph(pressure_point, patient):
    df = update_data(patient)
    fig = px.scatter(df[[f'l{pressure_point}',f'p{pressure_point}']])
    fig.update_layout(
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
    df = update_data(patient)

    data = df[['l0', 'l1', 'l2', 'p0', 'p1', 'p2']]
    if selected_stat == '1':
        data = data.max()
    elif selected_stat == '2':
        data = data.min()
    elif selected_stat == '3':
        data = data.mean()
        
    figure = {
        'data': [{
            'x': ['L0', 'L1', 'L2', 'R0', 'R1', 'R2'],
            'y': data,
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
    api_link = API + 'patients/' + str(patient_number)
    data = requests.get(api_link).json()[0]
    return data['birthdate'], data['disabled'], data['firstname'], data['lastname']

@app.callback(
    Output(component_id='time-graph', component_property='figure'),
    Output(component_id='time-slider', component_property='max'),
    Output(component_id='time-stamp', component_property='children'),
    Input(component_id='time-slider', component_property='value'),
    Input(component_id='chose_patient',  component_property='value'))
def update_figure(time, patient):
    df = update_data(patient)

    time_stamp = df.iloc[int(time)]['date']

    data = df[['l0', 'l1', 'l2', 'p0', 'p1', 'p2']]
    records_count = len(data.index)
    data = data.iloc[int(time)]



    figure = {
        'data': [{
            'x': ['L0', 'L1', 'L2', 'R0', 'R1', 'R2'],
            'y': data,
            'name': 'Maximal pressure'
        }],
        'layout': {
            'title': 'Pressure of every point in particural time-stamp',
        }
    }

    return figure, records_count, time_stamp

def update_data(patient_id):
    api_link = API + 'get/' + str(patient_id)
    data = pd.read_json(api_link)
    return pd.DataFrame(data)


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050, debug=True)
