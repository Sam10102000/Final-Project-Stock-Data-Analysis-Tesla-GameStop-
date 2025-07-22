import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(x=tesla_history['Date'], y=tesla_history['Close'], name="Stock Price"))
fig.add_trace(go.Scatter(x=pd.to_datetime(tesla_revenue['Date']), y=tesla_revenue['Revenue'].astype(float), name="Revenue"))

fig.update_layout(title="Tesla Stock Price and Revenue", xaxis_title="Date", yaxis_title="USD")
fig.show()
