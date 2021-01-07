import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash(__name__)

t = np.arange(0,100,0.1)
y_1=np.sin(t)
y_2=np.cos(t)

fig=go.Figure()
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
    yaxis={'range': [-3,3]}, 
    xaxis={'range': [0,100]},
    title='Left-rifght foot comparison',
    xaxis_title="Time",
    yaxis_title="Pressure",
    legend_title="Legend",
    )

app.layout = html.Div(children=[
    html.H1(children='Orthopedist\'s aplication for movement analysis'),

    html.Hr(),

    html.A("Patient 1", href='http://localhost:8050'),
    html.A("Patient 2", href='http://localhost:8050'),
    html.A("Patient 3", href='http://localhost:8050'),
    html.A("Patient 4", href='http://localhost:8050'),
    html.A("Patient 5", href='http://localhost:8050'),
    html.A("Patient 6", href='http://localhost:8050'),

    html.Hr(),

    html.H3(children='Patient 1, real-time data:'),    
  
    dcc.Graph(
        id='left_right_graph',
        figure=fig
    ),
    dcc.RadioItems(
        id='chose_left_right',
        options=[
            {'label': 'Pressure point 1', 'value': '1'},
            {'label': 'Pressure point 2', 'value': '2'},
            {'label': 'Pressure point 3', 'value': '3'}
        ],
        value='max'
    ),

    html.Hr(),

    dcc.Graph(
        id='statistical_graph',
        figure={
            'data': [
                {'x': ['L0', 'L1', 'L2', 'R0', 'R1' , 'R2'], 'y': [1024, 1036, 1072, 965, 1055, 1000],
                'type': 'bar', 'name': 'Maximal pressure'},
            ],
            'layout': {
                'title': 'Statistical data about foot pressure points',
            }
        }
    ),
    dcc.RadioItems(
        id='chose_statstical_data',
        options=[
            {'label': 'Maximal value', 'value': 'max'},
            {'label': 'Minimal value', 'value': 'min'},
            {'label': 'Mean value', 'value': 'mean'}
        ],
        value='max'
    )
])
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050, debug=True)