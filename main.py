#%% Resume Project 1import pandas as pdimport yfinance as yffrom yahoofinancials import YahooFinancialsimport datetimefrom dateutil.relativedelta import relativedelta#%% Import Datanow = datetime.datetime.now()start = now + relativedelta(years=-2) + relativedelta(days=1)data = yf.download('SPY ',                   interval='1h',                   start=start,                    #end=,                   auto_adjust = True,                   progress=True)#%%if __name__ == "__main__":   print("im a bg")