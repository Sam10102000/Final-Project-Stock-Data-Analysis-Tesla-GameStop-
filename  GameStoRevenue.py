
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table')
gme_revenue = pd.read_html(str(tables[1]))[0]

gme_revenue.columns = ['Date', 'Revenue']
gme_revenue = gme_revenue[gme_revenue['Revenue'] != '']
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace('$', '').str.replace(',', '')
gme_revenue.head()
