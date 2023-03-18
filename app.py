import plotly.express as px
import pandas as pd

df = pd.read_excel('BOPIS_09-03-2023.xlsx')


fig = px.line(df, x='LOJA', y='LEAD TIME', labels={
    'LOJAS' : 'LOJAS',
    'LEAD TIME' : 'HORAS'
}, color_discrete_sequence=px.colors.qualitative.T10, template='plotly_dark', text='LEAD TIME')

fig.update_traces(textposition='top center',texttemplate='%{text:.1f}')
fig.update_yaxes(showticklabels=False)
fig.update_layout(title={
 
    'text' : '''BOPIS: LEAD TIME DE FATURAMENTO\nDIA: 08/03/2023
    ''',
    'y' : 0.9,
    'x' : 0.5,
})

fig.show()