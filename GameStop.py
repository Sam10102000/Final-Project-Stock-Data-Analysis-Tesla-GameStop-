
gamestop = yf.Ticker("GME")
gme_history = gamestop.history(period="max")
gme_history.reset_index(inplace=True)

gme_history.head()
