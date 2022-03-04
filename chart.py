import plotly.graph_objs as go
import pandas as pd



def create_plot(symbol):
    df = pd.read_csv('data/{}.csv'.format(symbol))


    candlestick = go.Candlestick(x=df['date'],
                                     open=df['open'],
                                     high=df['high'],
                                     low=df['low'],
                                     close=df['close'])

    figure = go.Figure(data=[candlestick])

    # Gets rid of the weekends
    figure.layout.xaxis.type = 'category'

    shapes = [

        dict(x0='2022-02-22', x1='2022-02-22', y0=0, y1=1, xref='x', yref='paper'),
        dict(x0='2021-08-30', x1='2021-08-30', y0=0, y1=1, xref='x', yref='paper'),
        dict(x0='2021-05-03', x1='2021-05-03', y0=0, y1=1, xref='x', yref='paper'),
        dict(x0='2021-01-06', x1='2021-01-06', y0=0, y1=1, xref='x', yref='paper'),
        dict(x0='2021-01-26', x1='2021-01-26', y0=0, y1=1, xref='x', yref='paper'),
        dict(x0='2020-01-22', x1='2020-01-22', y0=0, y1=1, xref='x', yref='paper')
    ]

    annotations=[

        dict(x='2022-02-22', y=0.2, xref='x', yref='paper', showarrow=True, xanchor='right', text='Russia Invades Ukraine', bgcolor='lightgreen'),
        dict(x='2021-08-30', y=0.8, xref='x', yref='paper', showarrow=True, xanchor='right', text='USA Completes '
                                                                                              'Withdrawal From '
                                                                                              'Afghanistan', bgcolor='mistyrose'),
        dict(x='2021-05-03', y=0.7, xref='x', yref='paper', showarrow=True, xanchor='right', text='Trump\'s Deadline for Aghanistan Withdrawal', bgcolor='mistyrose'),
        dict(x='2021-01-06', y=0.05, xref='x', yref='paper', showarrow=True, xanchor='right', text='Storming Of the USA Capitol', bgcolor='lightgreen'),
        dict(x='2021-01-26', y=0.1, xref='x', yref='paper', showarrow=True, xanchor='left', text='Release of Q4 2020 Earnings', bgcolor='lightgreen'),
        dict(x='2020-01-22', y=0.85, xref='x', yref='paper', showarrow=True, xanchor='left', text='First Confirmed Case of COVID-19 in USA', bgcolor='mistyrose')
    ]

    figure.update_layout(title="{} Stock 2020 - 2022".format(symbol), annotations=annotations, shapes=shapes)
    figure.write_html(symbol+".html", auto_open=True)

create_plot("RTX")
create_plot("LMT")
