from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Таблица
df4 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
def generate_table(dataframe, max_rows=10):
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
# Линейный график (--- требует замену)
df1 = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig1 = px.line(df1, x="Fruit", y="Amount", color="City")
# Гистограмма
df3 = pd.read_csv('https://raw.githubusercontent.com/Anonim19992/dashboardproject/test/profit_analysis.csv')
fig3 = px.histogram(df3, x="Итого", y="Показатели прибыли", barmode="group")
# График рассеяния
df5 = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 3, 4],
    "size": [2, 1, 2, 2, 2, 1],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig5 = px.scatter(df5, x="Fruit", y="Amount", color="City", size="size")
# Круговая диаграмма (+++)
df6 = pd.read_csv('https://raw.githubusercontent.com/Anonim19992/dashboardproject/test/expenses.csv')
fig6 = px.pie(df6, values='Расходы', names='Статьи')

app.layout = html.Div(children=[
    generate_table(df4),
    dcc.Graph(
        id='example-graph-6',
        figure=fig6
    ),
    dcc.Graph(
        id='example-graph-5',
        figure=fig5
    ),
    dcc.Graph(
        id='example-graph-3',
        figure=fig3
    ),
    dcc.Graph(
        id='example-graph',
        figure=fig1
    )
])

if __name__ == '__main__':
    app.run(debug=True)