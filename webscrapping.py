import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {'user-agent':'Mozilla/5.0 \
            (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/84.0.4147.105 Safari/537.36'}

urls = [
        'https://www.google.com/finance/quote/NVDA:NASDAQ?sa=X&ved=2ahUKEwjY0Zf0luCIAxVmzTgGHZAdHxUQ3ecFegQIQhAh',
        'https://www.google.com/finance/quote/AAPL:NASDAQ',
        'https://www.google.com/finance/quote/ADBE:NASDAQ',
        'https://www.google.com/finance/quote/INTC:NASDAQ'
    ]

all=[]
for url in urls:
    page = requests.get(url,headers=headers)
    try:
        soup = BeautifulSoup(page.text, 'html.parser')
        company = soup.find('div', {'class': 'zzDege'}).text
        price = soup.find('div', {'class': 'YMlKec fxKbKc'}).text
        market_cap = soup.find('div', {'class': 'mfs7Fc'}).text
        # change = soup.find('span', {'class': 'JwB6zf Ez2Ioe P2Luy DnMTof'}).text
        # volume=soup.find('table', {'class': 'tb10Table col l5'}).find_all('td')[1].text
        x=[company, price, market_cap]
        all.append(x)

    except AttributeError:
      print("Change the Element id")
    # Wait for a short time to avoid rate limiting
    time.sleep(10)

# This code is modified by Susobhan Akhuli

column_names = ["Company", "Price", "Market Cap"]
df = pd.DataFrame(columns = column_names)

for i in all:
  index=0
  df.loc[index] = i
  df.index = df.index + 1
df=df.reset_index(drop=True)
df.to_excel('stocks.xlsx')