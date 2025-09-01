import yfinance as yf
import pandas as pd
import time

a = pd.read_csv("Tickers_and_Companies.csv", index_col="Company Name")

tickers = a['Ticker'].values
company_names = a.index.values


data_list_2y = []
data_list_5y = []
data_list_max = []


for ticker ,company_name in zip(tickers,company_names):
    try:
        stock  = yf.Ticker(ticker)
        historical_data_2y = stock.history(period="2y")
        historical_data_2y['Company Name'] = company_name
        historical_data_2y['Ticker'] = ticker
        
        stock  = yf.Ticker(ticker)
        historical_data_5y = stock.history(period="5y")
        historical_data_5y['Company Name'] = company_name
        historical_data_5y['Ticker'] = ticker
        
        stock  = yf.Ticker(ticker)
        historical_data_max = stock.history(period="max")
        historical_data_max['Company Name'] = company_name
        historical_data_max['Ticker'] = ticker
        
        data_list_2y.append(historical_data_2y)
        data_list_5y.append(historical_data_5y)
        data_list_max.append(historical_data_max)
        
        time.sleep(2)
    except Exception as e:
        print(f"Error fetching Data for {ticker} : {e}")
        continue
    
    
final_data_2y =pd.concat(data_list_2y)
final_data_5y =pd.concat(data_list_5y)
final_data_max =pd.concat(data_list_max)


final_data_2y.to_csv("stock_data_with_history_2y.csv", index=False)
final_data_5y.to_csv("stock_data_with_history_5y.csv", index=False)
final_data_max.to_csv("stock_data_with_history_max.csv", index=False)


print("Stock data for 2 years has been saved to stock_data_2y.csv")
print("Stock data for 5 years has been saved to stock_data_5y.csv")
print("Stock data for max period has been saved to stock_data_max.csv")
