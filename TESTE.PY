import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd



df = pd.read_excel('BOPIS_09-03-2023.xlsx', sheet_name='VENDAS')

trace1 = go.Bar(
    x=df['LOJA'],
    y=df['VL. FATURADO'],
    name='VL. FATURADO',
    marker=dict(color='#0f73ff') # set the marker color to silver
)
trace2 = go.Bar(
    x=df['LOJA'],
    y=df['VL. CANCELADO'],
    name='VL. CANCELADO',
    marker=dict(color='#cc1d23') # set the marker color to bronze
)
data = [trace1, trace2]
layout = go.Layout(
    title='2018 Winter Olympic Medals by Country'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar2.html')