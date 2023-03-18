from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background' : '#79bfc0',
    'text' : '#000000'
}

df = pd.read_excel('BOPIS_10-03-2023.xlsx', sheet_name='LT. FAT. MES')

fig = px.line(df, x="LOJA", y="LEAD TIME", labels= {
    'LOJA' : 'LOJAS',
    'LEAD TIME' : 'HORAS'
},color_discrete_sequence=px.colors.qualitative.T10,template='xgridoff',text='LEAD TIME')
fig.update_traces(textposition='top center',texttemplate='%{text:.1f}')
fig.update_yaxes(showticklabels=False)

fig.update_layout(
    plot_bgcolor = colors['background'],
    paper_bgcolor = colors['background'],
    font_color = colors['text']
)


app.layout = html.Div(style = {'backgroundColor' : colors ['background']}, children=[
    html.H1(
        children='BOPIS: LEAD TIME DE FATURAMENTO',
        style = {
            'textAlign' : 'center',
            'color' : colors ['text']   
        }
    ),

    html.Div(children= 'ACUMULADO MARÇO/23', style = {
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
