from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Таблица (+++)
df4 = pd.read_csv('https://raw.githubusercontent.com/Anonim19992/dashboardproject/test/data_table.csv')
def generate_table(dataframe, max_rows=7):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
# Гистограмма (+++)
df3 = pd.read_csv('https://raw.githubusercontent.com/Anonim19992/dashboardproject/test/profit_analysis.csv')
fig3 = px.histogram(df3, x="2021", y="2022", color="Показатели прибыли")
# График рассеяния (+++)
df5 = pd.read_csv('https://github.com/Anonim19992/dashboardproject/raw/test/correlation_analysis.csv')
fig5 = px.scatter(df5, x="2021", y="2022", color="Показатели прибыли", size="% влияния")
# Круговая диаграмма (+++)
df6 = pd.read_csv('https://raw.githubusercontent.com/Anonim19992/dashboardproject/test/expenses.csv')
fig6 = px.pie(df6, values='Расходы', names='Статьи')
# Слайдер (+++)


app.layout = html.Div(children=[
    html.H1(children='Процесс управления автопарком'),
    html.Div(children='------------------------------------------------------------'),
    html.Div(children='Таблица с данными для отображения ключевых финансовых показателей'),
    html.Div(children='------------------------------------------------------------'),
    generate_table(df4),
    html.Div(children='------------------------------------------------------------'),
    html.Div(children='Круговая диаграмма для визуализации структуры расходов по категориям'),
    html.Div(children='------------------------------------------------------------'),
    dcc.Graph(
        id='example-graph-6',
        figure=fig6
    ),
    html.Div(children='------------------------------------------------------------'),
    html.Div(children='График рассеяния для анализа корреляции между прибылью и другими финансовыми параметрами'),
    html.Div(children='------------------------------------------------------------'),
    dcc.Graph(
        id='example-graph-5',
        figure = fig5
    ),
    html.Div(children='------------------------------------------------------------'),
    html.Div(children='Слайсер выбора показателей для графика рассеяния'),
    html.Div(children='------------------------------------------------------------'),
    dcc.Slider(
        df5['2021'].min(),
        df5['2021'].max(),
        step=None,
        value=df5['2021'].min(),
        id='data_2021-slider'
    ),
    html.Div(children='------------------------------------------------------------'),
    html.Div(children='Гистограмма для анализа прибыли и ее распределения'),
    html.Div(children='------------------------------------------------------------'),
    dcc.Graph(
        id='example-graph-3',
        figure=fig3
    )
])


@callback(
    Output('example-graph-5', 'figure'),
    Input('data_2021-slider', 'value')
)

def update_graf(value):
    chart_data = df5[df5['2021'] > value]
    fig5 = px.scatter(chart_data, x="2021", y="2022", color="Показатели прибыли", size="% влияния")
    return fig5

if __name__ == '__main__':
    app.run(debug=True)