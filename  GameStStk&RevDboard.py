
fig = go.Figure()

fig.add_trace(go.Scatter(x=gme_history['Date'], y=gme_history['Close'], name="Stock Price"))
fig.add_trace(go.Scatter(x=pd.to_datetime(gme_revenue['Date']), y=gme_revenue['Revenue'].astype(float), name="Revenue"))

fig.update_layout(title="GameStop Stock Price and Revenue", xaxis_title="Date", yaxis_title="USD")
fig.show()
