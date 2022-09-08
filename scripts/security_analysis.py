import pandas as pd
import numpy as np
import pandas_datareader.data as web
from src.perf_metrics import PerfMetrics

start_date = pd.to_datetime('01 April 2020')
end_date = pd.to_datetime('31 March 2022')
print(start_date, end_date)
print(type(start_date))
print(start_date.strftime('%A')) # printing the day of the week
print(start_date + pd.to_timedelta(np.arange(10),'D')) #we can do NumPy-style vectorized operations directly on this same object

#Using TESLA as stock of interest
tsla_df = web.DataReader('TSLA', 'yahoo', start_date, end_date)
print(tsla_df.head())
print(tsla_df.tail())
print(tsla_df['Close']) #Use Close Price to compute daily stock returns

pm = PerfMetrics() #create an instance of the class PerfMetrics
rtn_series_daily = pm.compute_daily_return(tsla_df['Close'])