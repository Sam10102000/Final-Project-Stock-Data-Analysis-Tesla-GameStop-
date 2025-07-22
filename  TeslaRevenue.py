
!pip install beautifulsoup4 lxml --quiet

import requests
from bs4 import BeautifulSoup

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table')
tesla_revenue = pd.read_html(str(tables[1]))[0]

tesla_revenue.columns = ['Date', 'Revenue']
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != '']
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace('$', '').str.replace(',', '')
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != '']
tesla_revenue.head()
