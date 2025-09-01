import requests
from bs4 import BeautifulSoup
import csv

URL = "https://stockanalysis.com/stocks/"
r = requests.get(URL)
#print(r.content)

if r.status_code != 200:
    print(f"Error: Unable to fetch the webpage (status code: {r.status_code})")
else:
    print("Successfully fetched the webpage")

soup = BeautifulSoup(r.content,"lxml")
#print(soup.prettify())
tickers = soup.find_all('td',class_='sym')
#print(tickers)
companies =  soup.find_all('td',class_='slw')
#print(companies)

if not tickers or not companies:
    print("Error, could not find ticker or company symbols")
else:
    print(f"Found {len(tickers)} and {len(companies)} companies")


ticker_list = [ticker.text.strip() for ticker in tickers]
company_list = [company.text.strip() for company in companies]

ticker_company_pairs = list(zip(ticker_list,company_list))

with open("Tickers_and_Companies.csv",'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Ticker','Company Name'])
    writer.writerows(ticker_company_pairs)
    
print(f"Successfully saved {len(ticker_company_pairs)} entries to 'Tickers_and_Companies.csv'")
