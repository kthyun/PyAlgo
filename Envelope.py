import numpy as np
import technical_indicators.technical_indicators as tai

import sys
import datetime 
import pandas as pd
import pandas.io.data as dataReader


Chart_Start_date = datetime.datetime(2014,12,2)
Chart_end_date = datetime.datetime(2015,12,2)
        
try :
    stock_code = "068400.KS"
    data_source = "yahoo"
    
    daily_data = dataReader.DataReader(stock_code, data_source, Chart_Start_date, Chart_end_date)

    daily_data['MA5'] = pd.stats.moments.rolling_mean(daily_data['Adj Close'], 5)
    daily_data['MA20'] = pd.stats.moments.rolling_mean(daily_data['Adj Close'], 20)
    daily_data['MA60'] = pd.stats.moments.rolling_mean(daily_data['Adj Close'], 60)
    daily_data['MA120'] = pd.stats.moments.rolling_mean(daily_data['Adj Close'], 120)
    

    print ("=============================================")
    print (daily_data.info())
    print ("=============================================")
    

    period = 20
    k = 0.2    

    print(type(tai.ma_env(daily_data['Adj Close'], period, k, 4)))
    
    daily_data.to_csv(stock_code + '.csv')
    
except:
    e = sys.exc_info()[0]
    print("except raise %s"%e)
    print("%s"%sys.exc_info()[1].args)
