import pandas as pd
import numpy as np
import pandas_datareader.data as web
from src.perf_metrics import PerfMetrics
import matplotlib.pyplot as plt # Display figures inline in Jupyter notebook
import seaborn as sns # Use seaborn style defaults and set the default figure size


start_date = pd.to_datetime('01 April 2020')
end_date = pd.to_datetime('31 March 2022')
print(start_date, end_date)
print(type(start_date))
print(start_date.strftime('%A')) # printing the day of the week
print(start_date + pd.to_timedelta(np.arange(10),'D')) #we can do NumPy-style vectorized operations directly on this same object

#Using TESLA as stock of interest
tsla_df = web.DataReader('TSLA', 'yahoo', start_date, end_date)
print(tsla_df.info())
print(tsla_df.head())
print(tsla_df.tail())
print(tsla_df['Close']) #Use Close Price to compute daily stock returns

pm = PerfMetrics() #create an instance of the class PerfMetrics
rtn_series_daily = pm.compute_daily_return(tsla_df['Close'])
rtn_series_daily = rtn_series_daily.dropna(inplace=False)
print(rtn_series_daily.head())
print(rtn_series_daily.index)
print(rtn_series_daily.values)

tsla_df['Daily_Rtn'] = rtn_series_daily
tsla_df.loc['2020'] # Access via datetimeindex
tsla_df.loc['01 APR 2020':'31 MAR 2021'] #Access via slicing with datetimeindex for FY2021 
tsla_df[['Close','Daily_Rtn']]
print(f"TELSA Stock Return is {np.round(pm.compute_return_percentage(tsla_df.loc['01 APR 2020':'31 MAR 2021']['Close']))}% for FY2021")
print(f"TELSA Stock Return is {np.round(pm.compute_return_percentage(tsla_df['Close']))}% from 1APR20 - 31MAR22")
print(f"Cumulative Return for TELSA Stock from 1APR20 - 31MAR22 is {pm.compute_cumulative_return(tsla_df['Daily_Rtn'])}")
print(f"Annualization Factor for TELSA Stock from 1APR20 - 31MAR22 is {pm.compute_annualization_factor(tsla_df['Daily_Rtn'],365.25)}")
print(f"Annualized Return for TELSA Stock from 1APR20 - 31MAR22 is {pm.compute_annualized_return(tsla_df['Daily_Rtn']) * 100}%")

#2 Days Rolling Returns
tsla_df['2D_Rolling_Rtn'] = pm.compute_rolling_return(tsla_df['Daily_Rtn'],2)
#1 Day Rolling Cumulative Returns
tsla_df['Rolling_Cmu_Rtn'] = pm.compute_rolling_cumulative_return(tsla_df['Daily_Rtn'])
tsla_df.head(10)



#Visualize the daily returns in a line chart for FY2021
sns.set(rc={'figure.figsize':(11, 4)})
cols_plot = ['Open', 'Close', 'Daily_Rtn']
axes = tsla_df.loc['01 APR 2020':'31 MAR 2021'][cols_plot].plot(marker='.', alpha=0.5, linestyle='-', figsize=(11, 9), subplots=True)








