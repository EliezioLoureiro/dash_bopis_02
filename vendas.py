from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


app = Dash(__name__)

colors = {
    'background' : '#79bfc0',
    'text' : '#000000'
}

df = pd.read_excel('BOPIS_10-03-2023.xlsx', sheet_name='VENDAS')

font_size = 16

trace1 = go.Bar(
    x=df['LOJA'],
    y=df['VL. FATURADO'],
    name='VL. FATURADO',
    marker=dict(color='#0f73ff') 
)
trace2 = go.Bar(
    x=df['LOJA'],
    y=df['VL. CANCELADO'],
    name='VL. CANCELADO',
    marker=dict(color='#cc1d23') 
)
data = [trace1, trace2]
layout = go.Layout(
     title_font=dict(size=font_size),
    font=dict(size=font_size),
    
)
fig = go.Figure(data=data, layout=layout)
fig.update_traces(textposition='outside', texttemplate='R$ %{y:,.2f}')
fig.update_yaxes(tickformat='$.2f', showticklabels=False)
fig.update_layout(
    hovermode='x unified',
    xaxis=dict(
        tickformat='%{value:,.2f}',
    )
)

# Formatação manual de valores com vírgula como separador decimal
fig.for_each_trace(lambda trace: trace.update(text=[f"R$ {x:,.2f}".replace(".", "*").replace(",", ".").replace("*", ",") for x in trace.y]))



fig.update_layout(
    plot_bgcolor = colors['background'],
    paper_bgcolor = colors['background'],
    font_color = colors['text']
)

app.layout = html.Div(style = {'backgroundColor' : colors ['background']}, children=[
    html.H1(
        children='BOPIS: VENDAS (FATURADO VS CANCELADO)',
        style = {
            'textAlign' : 'center',
            'color' : colors ['text']   
        }
    ),

    html.Div(children= 'DIA: 08/03/2023', style = {
        'textAlign' : 'center',
        'color' : colors ['text']
    }),
       

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)