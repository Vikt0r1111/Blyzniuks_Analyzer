import plotly.graph_objects as go

class Plotter:
    @staticmethod
    def plot_stock_data(stock_data):
        fig = go.Figure()
        fig.add_trace(go.Candlestick(x=stock_data.index,
                                     open=stock_data['Open'],
                                     high=stock_data['High'],
                                     low=stock_data['Low'],
                                     close=stock_data['Close'],
                                     name='Цінові свічки'))

        fig.update_layout(template='plotly_dark',
                          title='Графік ціни та технічного індикатора',
                          xaxis_title='Date',
                          yaxis_title='Price')
        fig.show()